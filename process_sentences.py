#import nlt
# k
from gensim.utils import simple_preprocess
import random

def process_file(file):
    data = []
    for sent in file:
        data.append(simple_preprocess(sent))
    comments = [x for x in data if x]
    comments = [x for x in comments if x != ['deleted']]
    for i in range(5):
        print(random.choice(comments))

    return comments


