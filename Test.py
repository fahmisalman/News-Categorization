from nltk.stem.wordnet import WordNetLemmatizer

import glob
import re


bag = []

def lemmatization(token):
    lemma = WordNetLemmatizer()
    temp = []
    for i in range(len(token)):
        temp.append(lemma.lemmatize(token[i]))
    return temp

def stopwordRemoval(token):
    stopword = [line.rstrip('\n\r') for line in open('stopwords_en.txt')]
    temp = []
    for i in range(len(token)):
        if token[i] not in stopword:
            temp.append(token[i])
    return temp

if __name__ == '__main__':
    for name in glob.glob('bbc-2/sport/*'):
        file = open(name)
        s = file.read()
        s = s.lower()
        s = re.sub(r'[^a-z]', ' ', s)
        bag += s.split()
    bag = stopwordRemoval(bag)
    bag = lemmatization(bag)
    # print bag
    a = []
    for i in range(len(bag)):
        a.append(bag[i])
    print a