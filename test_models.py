import gensim
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


compass_wv = gensim.models.KeyedVectors.load('TWEC_master/model/compass.model')

from gensim.test.utils import datapath

wv_from_text = KeyedVectors.load_word2vec_format(datapath('word2vec_pre_kv_c'), binary=False)  # C text format
wv_from_bin = KeyedVectors.load_word2vec_format(datapath("euclidean_vectors.bin"), binary=True)  # C bin format

#import gensim.downloader as api

#test_word_vectors = api.load("glove-wiki-gigaword-100")
#test_result = word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])

print(compass_wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=5))
print()
print(compass_wv.most_similar(['noob'], topn=5))
print(compass_wv.most_similar(['wtf'], topn=5))
print(compass_wv.most_similar(['email'], topn=5))
print(compass_wv.most_similar(['hangry'], topn=5))
print()
print("Most similar to 'lol' ", compass_wv.most_similar(['lol'], topn=10))


pairs = [
    ('car', 'minivan'),   # a minivan is a kind of car
    ('car', 'bicycle'),   # still a wheeled vehicle
    ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    ('car', 'cereal'),    # ... and so on
    ('car', 'communism'),
    ('dog', 'poop'),
    ('rock', 'hard')
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))

print(compass_wv.most_similar(['feminism'], topn=20))
print(compass_wv.most_similar(positive=['mansplaining'], topn=20))
print(compass_wv.most_similar(positive=['binary', 'trans'], negative=['encoding'], topn=20))
print("Wholesome: ", compass_wv.most_similar(['wholesome'], topn=10))
print("Dank: ", compass_wv.most_similar(['dank'], topn=10))
print("Flex: ", compass_wv.most_similar(['flex'], topn=10))
print("Salty: ", compass_wv.most_similar(['salty'], topn=10))
print("Woke: ", compass_wv.most_similar(['woke'], topn=10))
print("fam: ", compass_wv.most_similar(['fam'], topn=10))
print("Swag: ", compass_wv.most_similar(['swag'], topn=10))