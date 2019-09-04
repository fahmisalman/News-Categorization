from __future__ import division
import Preprocessing
import glob
import re
import csv

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
    pre = Preprocessing.Preprocessing()
    bag = pre.stopwordRemoval(bag)
    bag = pre.lemmatization(bag)
    n += 1
    return bag, n

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

def saveToExcel(ws, column_cell, list, string):
    ws[column_cell + str(1)] = string
    for row, i in enumerate(list):
        ws[column_cell + str(row + 2)] = str(i)


if __name__ == '__main__':
    print "Load data .",
    sport, nSport = loadData('Dataset/sport/*'); print ".",
    business, nBusiness = loadData('Dataset/business/*'); print ".",
    politics, nPolitics = loadData('Dataset/politics/*'); print ".",
    entertainment, nEntertainment = loadData('Dataset/entertainment/*'); print ".",
    tech, nTech = loadData('Dataset/tech/*'); print "."

    print "Training .",
    # Prior
    n = nSport + nBusiness + nPolitics + nEntertainment + nTech
    nSport /= n
    nBusiness /= n
    nPolitics /= n
    nEntertainment /= n
    nTech /= n

    # Likelihood
    bag = sport + business + politics + entertainment + tech
    wordList = list(set(bag))
    likelihoodSport = likelihoodProbabilities(wordList, sport); print ".",
    likelihoodBusiness = likelihoodProbabilities(wordList, business); print ".",
    likelihoodPolitics = likelihoodProbabilities(wordList, politics); print ".",
    likelihoodEntertainment = likelihoodProbabilities(wordList, entertainment); print ".",
    likelihoodTech = likelihoodProbabilities(wordList, tech); print "."

    temp = []

    print "\nSaving data . . . ."

    with open("Prior.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows([['prior']])
        writer.writerows([[nSport]])
        writer.writerows([[nBusiness]])
        writer.writerows([[nPolitics]])
        writer.writerows([[nEntertainment]])
        writer.writerows([[nTech]])

    for i in range(len(wordList)):
        temp.append([wordList[i], likelihoodSport[i], likelihoodBusiness[i], likelihoodPolitics[i], likelihoodEntertainment[i], likelihoodTech[i]])
    with open("Likelihood.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows([['words', 'sport', 'business', 'politic', 'entertainment', 'tech']])
        writer.writerows(temp)
