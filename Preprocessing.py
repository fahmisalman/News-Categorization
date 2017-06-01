from __builtin__ import object
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *


class Preprocessing(object):

    def __init__(self):
        self

    def tokenisasi(self, sentence):
        return sentence.split()

    def lemmatization(self, token):
        lemma = WordNetLemmatizer()
        stemmer = PorterStemmer()
        temp = []
        for i in range(len(token)):
            word = stemmer.stem(token[i])
            temp.append(lemma.lemmatize(word))
        return temp

    def stopwordRemoval(self, token):
        stopword = [line.rstrip('\n\r') for line in open('stopwords_en.txt')]
        temp = []
        for i in range(len(token)):
            if token[i] not in stopword:
                temp.append(token[i])
        return temp