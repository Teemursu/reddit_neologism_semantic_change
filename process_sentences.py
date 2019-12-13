from gensim.utils import simple_preprocess
import random
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

def process_file(file):
    '''
    1) Convert sentences into a list of lowercase tokens, ignoring tokens that are too short or too long.
    2) Filter out deleted/removed comments, empty lines and stop words
    '''
    comments = []
    for sent in file:
        comments.append(simple_preprocess(sent))
    get_rid_of_these = {'http', 'com', 'https', 'html'}
    comments = [x for x in comments if x != ['deleted'] and x != 'removed']
    comments[:] = [[word for word in sub if word not in get_rid_of_these] for sub in comments]
    comments[:] = [[word for word in sub if word not in stopwords] for sub in comments]
    comments = [x for x in comments if x]

    print("... Showing a random comment...")
    for i in range(1):
        print(random.choice(comments))
    return comments

"""
file = open('comment_data/test.txt')
process_file(file)
"""