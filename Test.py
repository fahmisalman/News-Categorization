from __future__ import division
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *

import glob
import re

def loadData(location):
    bag = []
    n = 0
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

def likelihoodProbabilities(list, bag):
    likelihood = []
    for i in range(len(list)):
        likelihood.append(bag.count(list[i]))
    for i in range(len(likelihood)):
        likelihood[i] += 1
    total = sum(likelihood)
    for i in range(len(likelihood)):
        likelihood[i] /= total
    return likelihood

if __name__ == '__main__':
    sport, nSport = loadData('bbc-2/sport/001.txt')
    business, nBusiness = loadData('bbc-2/business/001.txt')
    politics, nPolitics = loadData('bbc-2/politics/001.txt')
    entertainment, nEntertainment = loadData('bbc-2/entertainment/001.txt')
    tech, nTech = loadData('bbc-2/tech/001.txt')
    bag = sport + business + politics + entertainment + tech
    wordList = list(set(bag))
    likelihoodSport = likelihoodProbabilities(wordList, sport)
    likelihoodBusiness = likelihoodProbabilities(wordList, business)
    likelihoodPolitics = likelihoodProbabilities(wordList, politics)
    likelihoodEntertainment = likelihoodProbabilities(wordList, entertainment)
    likelihoodTech = likelihoodProbabilities(wordList, tech)