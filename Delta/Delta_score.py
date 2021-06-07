import os
import nltk
import math
import matplotlib.pyplot as plt
import numpy as np

def read_files_into_string(datapath, filenames):
    strings = []
    for file in filenames:
        with open(datapath + '/' + file) as f:
            strings.append(f.read())
    return '\n'.join(strings)


# function to build list of filename per author
def get_filenames_per_author_into_dict(datapath):
    list_of_files = os.listdir(datapath)
    store = list()
    for i in list_of_files:
        store.append(i.split('_')[0])
    authors = list(set(store))
    storage = {}
    count = 0
    for a in authors:
        store2 = list()
        for f in list_of_files:
            if f.startswith(a):
                store2.append(f)
            else:
                continue
        storage[authors[count]] = store2
        count += 1
        
    return storage

# put every author into a single string in a dict
def get_single_string_per_author_into_dict(datapath):
    x = get_filenames_per_author_into_dict(datapath)
    authors = list(x.keys())
    strings_by_author = {}
    
    for author in authors:
        strings_by_author[author] = read_files_into_string(datapath, x[author])

    return strings_by_author


# transform authors' corpora into lists of word tokens
def get_tokens_by_author(datapath):
    # call function to process data first
    strings = get_single_string_per_author_into_dict(datapath)
    authors = strings.keys()
    
    # storage variables
    length_distribution = []
    sorted_length = []
    author_tokens = {}
    author_length_distributions = {}
    
    for author in authors:
        tokens = nltk.word_tokenize(strings[author], language = 'italian')
    
    # Filter out punctuation
        author_tokens[author] = ([token for token in tokens if any(c.isalpha() for c in token)])

    # Get a distribution of token lengths
        token_lengths = [len(token) for token in author_tokens[author]]
        author_length_distributions[author] = nltk.FreqDist(token_lengths)
    #author_length_distributions[author].plot(15,title=author)
        sorted_length.append((dict(sorted((dict(author_length_distributions[author])).items()))))
        length_distribution.append(author_length_distributions[author])
    
    return {"length_distribution": length_distribution, "sorted_length": sorted_length, "author_tokens": author_tokens, "author_length_distributions": author_length_distributions}
