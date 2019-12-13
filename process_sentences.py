from gensim.utils import simple_preprocess
import random
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

def process_file(file):
    data = []
    comments=[]
    for sent in file:
        data.append(simple_preprocess(sent))
    for review in data:
        wr = []
        for word in review:
            if word not in stopwords:
                wr.append(word)
            comments.append(wr)
    comments = [x for x in comments if x]
    comments = [x for x in comments if x != ['deleted']]

    for i in range(5):
        print(random.choice(comments))

    return comments

"""
file = open('comment_data/test.txt')
process_file(file)
"""