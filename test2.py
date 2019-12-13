import gensim
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


word_vectors = gensim.models.KeyedVectors.load('TWEC_master/model/arxiv_9.model')

from gensim.test.utils import datapath

wv_from_text = KeyedVectors.load_word2vec_format(datapath('word2vec_pre_kv_c'), binary=False)  # C text format
wv_from_bin = KeyedVectors.load_word2vec_format(datapath("euclidean_vectors.bin"), binary=True)  # C bin format

#import gensim.downloader as api

#test_word_vectors = api.load("glove-wiki-gigaword-100")
#test_result = word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])

word = 'reddit'
result = word_vectors.most_similar([word], topn=10)
print("The words most similar to '" + word + "' are ", result)
