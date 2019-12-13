import gensim
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


wv = gensim.models.KeyedVectors.load('TWEC_master/model/data2009-01.model')

from gensim.test.utils import datapath

wv_from_text = KeyedVectors.load_word2vec_format(datapath('word2vec_pre_kv_c'), binary=False)  # C text format
wv_from_bin = KeyedVectors.load_word2vec_format(datapath("euclidean_vectors.bin"), binary=True)  # C bin format

#import gensim.downloader as api

#test_word_vectors = api.load("glove-wiki-gigaword-100")
#test_result = word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])

print(wv.most_similar(positive=['minivan', 'car'], negative=['bicycle'], topn=5))
print()
print(wv.most_similar(positive=['noob'], negative=['ugh'], topn=5))
print()
print("Most similar to 'lol' ", wv.most_similar(['lol'], topn=10))

pairs = [
    ('car', 'minivan'),   # a minivan is a kind of car
    ('car', 'bicycle'),   # still a wheeled vehicle
    ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    ('car', 'cereal'),    # ... and so on
    ('car', 'communism'),
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))