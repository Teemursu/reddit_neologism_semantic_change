#import bz2file # import this if a file extension is .bz2
import json
from gensim.utils import simple_preprocess
import numpy
import lzma
import create_compass

def get_sentences(year, month):
    '''
    Read the JSON data files and
    return a list of all the 'body' values (comments)
    for that year and month
    '''

    """
    Define our directory for the Reddit corpus
    that currently exists on an external hard drive.

    The "reddit_data" directory contains subdirectories
    which are named as years during which the comments have been made.
    """

    """"
    Each folder for the year contains a compressed JSON (.bz2) file
    that has all the comments posted that month. E.g. "RC_2008-06.bz2"
    """

    # Note the file extension above. Some of the encoded corpus files maybe .bz2, .xz or in other formats.
    filename = "RC_" + str(year) + "-" + str(month) + ".xz"
    print("...Reading the file '" + filename+"'...")

    # bz2file.open() to open a file with a .bz2 extension,
    with lzma.open("comment_data/tobewrited" + "\\" + filename, 'r',
                        ) as f:
        print("File opened successfully!")
        count = 0
        for i, line in enumerate(f):
            test = numpy.random.randint(2, size=1) # Quick (inefficient) workaround to get semi-random comments
            if test != 0:
                data = json.loads(line)
                data = {k: v for k, v in data.items() if k == 'body'}
                if data['body'] != '':
                    if data['body'] != '[deleted]' and line != '[removed]':
                        with open("comment_data/1-mil-comm-per-month/one-mil-comments-" + year + "-" + month + ".txt",
                                  "a", encoding='utf-8') as json_file:
                            json_file.write(str(" ".join(simple_preprocess(data['body']))))
                            json_file.write('\n')
                            count += 1
                            #print(count)
                            if count > 1000000:
                                return
        f.close()
    print("...Successfully imported data from the file '" + filename+"'.")


years = ['2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017']
months = ['01', '02', '03', '04', '05', '06',
          '07', '08', '09', '10', '11', '12']

# Modify the list depending on which year/month slice(s) you want.
for year in years:
    for month in months:
        get_sentences(year, month)

# After preparing the sliced corpus, we can create the atemporal embedding upon which we align other embeddigns.
create_compass.get_compass()
