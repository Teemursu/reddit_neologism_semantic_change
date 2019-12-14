from twec.twec import TWEC
from gensim.models.word2vec import Word2Vec

# decleare a TWEC object, siter is the number of iterations of the compass, diter is the number of iterations of each slice
aligner = TWEC(size=100, siter=5, diter=5, workers=4)
# train the compass: the text should be the concatenation of the text from the slices
aligner.train_compass("C:\\Users\\temep\\PycharmProjects\\semantic_change\\TWEC_master\\examples\\training\\compass.txt", overwrite=True) # keep an eye on the overwrite behaviour

# now you can train slices and they will be already aligned
# these are gensim word2vec objects
#slice_one = aligner.train_slice("C:\\Users\\temep\\PycharmProjects\\semantic_change\\comment_data\\data2009-01.txt", save=True)
#slice_two = aligner.train_slice("comment_data/data2009-02.txt", save=True)
