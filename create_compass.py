import glob
import time


def get_compass():
    '''
    The TWEC requires a compass file
    which contains all of the processed text data
    '''
    read_files = glob.glob("C:\\Users\\temep\\PycharmProjects\\semantic_change\\comment_data\\1-mil-comm-per-month\\*.txt")

    with open("TWEC_master/examples/training/compass.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                print("Adding file " + str(f) + " into compass...")
                outfile.write(infile.read())

start = time.time()
print("Creating the compass...")
get_compass()
end = time.time()
print(end - start)
print("Compass created! Would you like to find out the total number of sentences? y/n")
answer = input(str())
if answer == 'y':
    start = time.time()
    print("Ok! Counting...")
    count = 0
    for line in open("TWEC_master/examples/training/compass.txt", encoding='utf-8').readlines(): count += 1
    print("There are " +count+ " sentences.")
    end = time.time()
    print(end - start)
else:
    pass


