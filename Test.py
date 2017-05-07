from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *

import glob
import re

def loadData(location):
    n = 0
    bag = []
    for name in glob.glob(location):
        file = open(name)
        s = file.read()
        s = s.lower()
        s = re.sub(r'[^a-z]', ' ', s)
        bag += s.split()
        n += 1
    bag = stopwordRemoval(bag)
    bag = lemmatization(bag)
    return bag, n

def lemmatization(token):
    lemma = WordNetLemmatizer()
    stemmer = PorterStemmer()
    temp = []
    for i in range(len(token)):
        word = stemmer.stem(token[i])
        temp.append(lemma.lemmatize(word))
    return temp

def stopwordRemoval(token):
    stopword = [line.rstrip('\n\r') for line in open('stopwords_en.txt')]
    temp = []
    for i in range(len(token)):
        if token[i] not in stopword:
            temp.append(token[i])
    return temp

if __name__ == '__main__':
    sport, nSport = loadData('bbc-2/sport/*')
    business, nBusiness = loadData('bbc-2/business/*')
    politics, nPolitics = loadData('bbc-2/politics/*')
    entertainment, nEntertainment = loadData('bbc-2/entertainment/*')
    tech, nTech = loadData('bbc-2/tech/*')
    bag = sport + business + politics + entertainment + tech
    print len(bag)
    wordList = list(set(bag))
    likelihood = []
    for i in range(len(wordList)):
        likelihood.append(bag.count(wordList[i]))
    print sum(likelihood)
