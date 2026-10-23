"""Baseline lexical reproduzível, sem API externa ou modelo generativo."""
import argparse
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path

def tokenize(text):
    text=unicodedata.normalize('NFKD',text.casefold())
    text=''.join(c for c in text if not unicodedata.combining(c))
    return re.findall(r'[a-z0-9]+',text)

def search(query,documents,limit=3):
    if limit<1: raise ValueError('limit deve ser positivo')
    counts=[Counter(tokenize(doc['text'])) for doc in documents]
    if not counts: return []
    frequencies=Counter(term for count in counts for term in count)
    idf={term:math.log((len(counts)+1)/(freq+1))+1 for term,freq in frequencies.items()}
    def vector(tokens):
        values={term:count*idf[term] for term,count in tokens.items() if term in idf}
        norm=math.sqrt(sum(value*value for value in values.values()))
        return {term:value/norm for term,value in values.items()} if norm else {}
    q=vector(Counter(tokenize(query)))
    results=[]
    for doc,count in zip(documents,counts):
        d=vector(count); score=sum(value*d.get(term,0) for term,value in q.items())
        if score>0: results.append({'id':doc['id'],'score':score,'text':doc['text']})
    return sorted(results,key=lambda item:(-item['score'],item['id']))[:limit]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    parser.add_argument('--documents',type=Path,default=Path(__file__).with_name('documentos.json'))
    args=parser.parse_args()
    print(json.dumps(search(args.query,json.loads(args.documents.read_text(encoding='utf-8'))),ensure_ascii=False,indent=2))

if __name__=='__main__': main()
