# Busca lexical: baseline para comparar com embeddings

Implementação didática de TF-IDF e similaridade de cosseno em Python 3.11+, sem dependências externas.

```sh
python experimentos/busca_lexical.py "testes automatizados"
python -m unittest discover -s tests -v
```
O primeiro comando retorna documentos e scores; o segundo verifica normalização, ordenação, ausência de correspondência e limite. É busca lexical, não busca semântica: sinônimos sem termos compartilhados podem não retornar resultados.

Próxima comparação: usar o mesmo corpus e consultas rotuladas com embeddings, medir Recall@k, latência e custo. Não há benchmark de qualidade nem resultados de um modelo de embeddings nesta entrega.
