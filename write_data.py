import bz2file
import json
import os
import process_data
import process_sentences
from gensim.utils import simple_preprocess


def get_sentences(year, month):
    DATA_DIR = os.path.join("D:\\", "reddit", "reddit_data", str(year))
    filename = "RC_" + str(year) + "-" + str(month) + ".bz2"
    sentences = []

    print(DATA_DIR + "\\" + filename)
    print("Reading the file '" + DATA_DIR + "\\" + filename)

    with bz2file.open(DATA_DIR + "\\" + filename, 'r',
                        compresslevel=9,
                        encoding=None,
                        errors=None,
                        newline=None) as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            sentences.append(data['body'])
        f.close()
    print("Successfully imported data from the file '" + filename+"'.")
    return sentences


def write_data(year, month, comments):
    print("Writing data for " + year + "/" + month + " sentences")

    with open("comment_data/data" + year + "-" + month + ".txt", "w", encoding='utf-8') as json_f:
        json_f.write("\n".join([' '.join(map(str, item)) for item in comments]))
        json_f.close()
        #json.dump(sentences, json_f)
        #json_f.write("\n")


years = ['2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017']
months = ['01', '02', '03', '04', '05', '06',
          '07', '08', '09', '10', '11', '12']

test_years = ['2009']
test_months = ['01', '02', '12']

for year in test_years:
    for month in test_months:
        sentences = get_sentences(year, month)
        comments = process_sentences.process_file(sentences)
        write_data(year, month, comments)



