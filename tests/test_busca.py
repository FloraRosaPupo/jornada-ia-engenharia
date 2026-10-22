import unittest
from experimentos.busca_lexical import search,tokenize
class SearchTests(unittest.TestCase):
    def test_normaliza_acentos(self):
        self.assertEqual(tokenize('Integração CONTÍNUA'),['integracao','continua'])
    def test_ordena_por_relevancia(self):
        docs=[{'id':'a','text':'banana maçã'},{'id':'b','text':'testes testes software'}]
        self.assertEqual(search('testes',docs)[0]['id'],'b')
    def test_sem_correspondencia_nao_inventa_resultado(self):
        self.assertEqual(search('python',[{'id':'a','text':'banana'}]),[])
    def test_consulta_vazia(self):
        self.assertEqual(search('',[{'id':'a','text':'banana'}]),[])
    def test_limite(self):
        self.assertEqual(len(search('a',[{'id':str(i),'text':'a'} for i in range(4)],limit=2)),2)
if __name__=='__main__':unittest.main()
