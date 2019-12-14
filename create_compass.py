import glob
import time


def get_compass():
    '''
    The TEWC requires a compass file
    which contains all of the processed text data
    '''
    read_files = glob.glob("D:\\reddit\\reddit_data\\extracted\\no_stopwords\\*.txt")

    with open("TWEC_master/examples/training/compass.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

start = time.time()
get_compass()
end = time.time()
print(end - start)
