import bz2file
import json
import os
import process_sentences


def get_sentences(year, month):
    '''
    Read the JSON data files and
    return a list of all the 'body' values (comments)
    for that year and month
    '''

    sentences = []

    """
    Define our directory for the Reddit corpus
    that currently exists on an external hard drive.

    The "reddit_data" directory contains subdirectories
    which are named as years during which the comments have been made.
    """
    DATA_DIR = os.path.join("D:\\", "reddit", "reddit_data", str(year))

    """"
    Each folder for the year contains a compressed JSON (.bz2) file
    that has all the comments posted that month. E.g. "RC_2008-06.bz2"
    """
    filename = "RC_" + str(year) + "-" + str(month) + ".bz2"

    print("Let's look at " + DATA_DIR + "\\" + filename + "...")
    print()
    print("...Reading the file '" + filename+"'...")
    with bz2file.open(DATA_DIR + "\\" + filename, 'r',
                        compresslevel=9,
                        encoding=None,
                        errors=None,
                        newline=None) as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            sentences.append(data['body'])
        f.close()
    print("...Successfully imported data from the file '" + filename+"'.")
    print()
    return sentences


def write_data(year, month, comments):
    '''
    Write a text file in which each line represents a sentence/comment.
    '''
    print("Writing data for comments made in " + year + "/" + month +"...")

    with open("comment_data/comments" + "-" + year + "-" + month + ".txt", "w", encoding='utf-8') as json_f:
        json_f.write("\n".join([' '.join(map(str, item)) for item in comments]))
        json_f.close()
        print("...Comment data file successfully created!")
        print()

'''
A list of years and months lets us loop through the data folders 
and specify which file to write the comments to.
'''
years = [ '2011',
         '2012', '2013', '2014', '2015', '2016', '2017']
months = ['01', '02', '03', '04', '05', '06',
          '07', '08', '09', '10', '11', '12']

test_years = ['2006', '2007', '2008', '2009', '2010',]
test_months = ['01', '02', '12']

'''
For each year, go through each month. For each of those months,
get the data, process the data and write it into a file that Word2Vec accepts.
'''
for year in years:
    for month in months:
        sentences = get_sentences(year, month)
        comments = process_sentences.process_file(sentences)
        write_data(year, month, comments)



