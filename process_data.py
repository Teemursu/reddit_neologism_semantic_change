import datetime

def get_date(data):
    for dictionary in data:
        for k in list(dictionary.keys()):
            if k == 'created_utc':
                timestamp = datetime.datetime.fromtimestamp(int(dictionary[k]))
                dictionary[k] = timestamp.strftime("%d.%m.%Y")

    return data


def remove_keys(data):
    for dictionary in data:
        for k in list(dictionary.keys()):
            if k not in {'body', 'subreddit', 'author', 'created_utc', 'comment', 'date'}:
                del dictionary[k]

    return data

def rename_keys(data):
    for dictionary in data:
        for k in list(dictionary.keys()):
            if k == 'body':
                dictionary['comment'] = dictionary.pop('body')
            if k == 'created_utc':
                dictionary['date'] = dictionary.pop('created_utc')

    return data

def get_comments(data):
    comments = []
    for dictionary in data:
        for k in list(dictionary.keys()):
            if k == 'body':
                comments.append(dictionary['body'])

    return comments
