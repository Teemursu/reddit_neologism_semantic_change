from twec.twec import TWEC
from gensim.models.word2vec import Word2Vec
import glob

"""
def train_data(year, month, comments):
    '''
    Write a text file in which each line represents a sentence/comment.
    '''
    print("Writing data for comments made in " + year + "/" + month +"...")

    train_string = "\n".join([' '.join(map(str, item)) for item in comments])

    return train_string


def train(string):
    aligner.train_slice(string, save=True)
"""


print("Declaring the TWEC object...")
# decleare a TWEC object, siter is the number of iterations of the compass,
# diter is the number of iterations of each slice
aligner = TWEC(size=300, siter=10, diter=10, workers=4, min_count=2, window=10, ns=10, sg=0)
# train the compass: the text should be the concatenation of the text from the slices
print("Training the compass...")
aligner.train_compass("TWEC_master/examples/training/compass.txt", overwrite=True) # keep an eye on the overwrite behaviour
print("Training complete!")


# now you can train slices and they will be already aligned
# these are gensim word2vec objects
#slice_one = aligner.train_slice("C:\\Users\\temep\\PycharmProjects\\semantic_change\\comment_data\\data2009-01.txt", save=True)
#slice_two = aligner.train_slice("comment_data/data2009-02.txt", save=True)
print("Reading files...")
read_files = glob.glob("comment_data/1-mil-comm-per-month\\*.txt")

for file in read_files:
    print("Training the slice for " + str(file))
    aligner.train_slice(file, save=True, )
