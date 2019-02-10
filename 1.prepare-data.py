#!/usr/bin/env python

import os
import pandas
import pickle

# Location (root) of git@github.com:vsoch/hospital-chargemasters

base = "/home/vanessa/Documents/Dropbox/Code/database/hospital-chargemaster"
hospital_folders = os.listdir('%s/data' %base)

# Read in data latest to common data frame
columns = ['charge_code', 
           'price', 
           'description', 
           'hospital_id', 
           'filename', 
           'charge_type']

# Find latest data files
data_files = []
for folder in hospital_folders:
    data_file = "%s/data/%s/data-latest.tsv" %(base, folder)
    if os.path.exists(data_file):
        data_files.append(data_file)

# Create smaller set for now
data_files = data_files[0:1]
df = pandas.DataFrame(columns=columns)

for data_file in data_files:
    df_ = pandas.read_csv(data_file, sep='\t')
    df = df.append(df_)

################################################################################
# Preprocessing
################################################################################

from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import *
import re

def do_stem(words):
    '''use nltk porter stemmer to perform stemming
 
       Parameters
       ==========    
       words: str/list one or more words to be stemmed
    '''
    stemmer = PorterStemmer()
    if isinstance(words, str):
        words = [words]
    stems = []
    for word in words:
        word = remove_nonenglish_chars(word)
        if word.strip():
            stems.append(stemmer.stem(word))
    return stems

def remove_nonenglish_chars(text):
    return re.sub("[^a-zA-Z0-9]", " ", text).strip()

def sentence2words(sentence):
    # Make lowercase
    sentence = sentence.lower()
    # Split by white spaces
    re_white_space = re.compile("\s+")
    words = re_white_space.split(sentence.strip())
    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if w not in stop_words]
    return words
    

# For each sentence, stop word removal, etc.
corpus = []
for row in df.iterrows():
    description = row[1]['description'] 
    if not pandas.isnull(description):
        words = sentence2words(description)
        corpus.append(' '.join(words))

# Cut off based on words

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(X.toarray())

pickle.dump(corpus, open('corpus.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
pickle.dump(X, open('vectorizer-X.pkl', 'wb'))
