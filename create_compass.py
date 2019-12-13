import glob


def get_compass():
    '''
    The TEWC requires a compass file
    which contains all of the processed text data
    '''
    read_files = glob.glob("comment_data/*.txt")

    with open("TWEC_master/examples/training/compass.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())


get_compass()