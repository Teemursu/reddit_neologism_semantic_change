import glob

read_files = glob.glob("comment_data/*.txt")

with open("TWEC_master/examples/training/compass.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())