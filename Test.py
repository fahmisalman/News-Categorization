from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *

import glob
import re

def loadData(location, label):
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
    temp = []
    for i in range(len(bag)):
        temp.append([bag[i], label])
    return temp, n

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
    # for name in glob.glob('bbc-2/sport/*'):
    #     file = open(name)
    #     s = file.read()
    #     s = s.lower()
    #     s = re.sub(r'[^a-z]', ' ', s)
    #     bag += s.split()
    sportLoc = 'bbc-2/sport/*'
    businessLoc = 'bbc-2/business/*'
    politicsLoc = 'bbc-2/politics/*'
    entertainmentLoc = 'bbc-2/entertainment/*'
    techLoc = 'bbc-2/tech/*'
    sport, nSport = loadData(sportLoc, "sport")
    business, nBusiness = loadData(businessLoc, "business")
    politics, nPolitics = loadData(politicsLoc, "politics")
    entertainment, nEntertainment = loadData(entertainmentLoc, "entertainment")
    tech, nTech = loadData(techLoc, "tech")
    print nSport, nBusiness, nPolitics, nEntertainment, nTech
    print len(sport), len(business), len(politics), len(entertainment), len(tech)
    bag = sport + business + politics + entertainment + tech
    print len(bag)
    # bag = stopwordRemoval(bag)
    # bag, word = lemmatization(bag)
