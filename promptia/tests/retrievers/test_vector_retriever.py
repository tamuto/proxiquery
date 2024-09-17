import unittest

from sentence_transformers import SentenceTransformer

from promptia.retrievers.vector_retriever import LocalVectorProcessor
from promptia.retrievers.vector_retriever import VectorQuery


class TestCase(unittest.TestCase):

    def test_query(self):
        spm = SentenceTransformer('stsb-xlm-r-multilingual', device='cpu')
        proc = LocalVectorProcessor(spm)
        proc.load_index('../../assets/proxiquery', 'vector')
        query = VectorQuery(proc, 'アカウント')
        results = query.query()
        print(results)

    # 問題なかったので、コメントアウト
    # def test_make_index(self):
    #     spm = SentenceTransformer('stsb-xlm-r-multilingual', device='cpu')
    #     proc = LocalVectorProcessor(spm)
    #     proc.make_index('../../assets/proxiquery', 'dataset.json')
    #     proc.save_index('./env', 'vector')
    #     query = VectorQuery(proc, 'アカウント')
    #     results = query.query()
    #     print(results)
