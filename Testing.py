from __future__ import division
import csv
import Preprocessing
import glob
import math


def loadDataTrain():
    with open("Likelihood.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        words = []
        likelihood = []
        for row in reader:
            words.append(row['words'])
            likelihood.append([float(row['sport']), float(row['business']), float(row['politic']),
                               float(row['entertainment']), float(row['tech'])])
    with open("Prior.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        prior = []
        for row in reader:
            prior.append(float(row['prior']))
    return words, likelihood, prior


def loadData(words, likelihood, prior, location, kelas):
    pre = Preprocessing.Preprocessing()
    benar = 0
    jumlah = 0
    for name in glob.glob(location):
        file = open(name)
        x = file.read()
        x = pre.caseFolding(x)
        x = pre.tokenisasi(x)
        x = pre.stopwordRemoval(x)
        x = pre.lemmatization(x)
        probs = []
        for j in range(len(prior)):
            tmp = 0
            for i in range(len(x)):
                if x[i] in words:
                    temp = words.index(x[i])
                    tmp += math.log(likelihood[temp][j])
            tmp += math.log(prior[j])
            probs.append(tmp)
        higher = sorted(range(len(probs)), key=lambda k: probs[k], reverse=True)
        if higher[0] == 0:
            label = "sport"
        elif higher[0] == 1:
            label = "business"
        elif higher[0] == 2:
            label = "politic"
        elif higher[0] == 3:
            label = "entertainment"
        elif higher[0] == 4:
            label = "tech"
        if label == kelas:
            benar += 1
        jumlah += 1
    return benar, jumlah

if __name__ == '__main__':
    words, likelihood, prior = loadDataTrain()
    correct = 0
    total = 0
    benar, jumlah = loadData(words, likelihood, prior, 'bbc-2/sport/*', 'sport'); print ".",
    correct += benar
    total += jumlah
    benar, jumlah = loadData(words, likelihood, prior, 'bbc-2/business/*', 'business'); print ".",
    correct += benar
    total += jumlah
    benar, jumlah = loadData(words, likelihood, prior, 'bbc-2/politics/*', 'politic'); print ".",
    correct += benar
    total += jumlah
    benar, jumlah = loadData(words, likelihood, prior, 'bbc-2/entertainment/*', 'entertainment'); print ".",
    correct += benar
    total += jumlah
    benar, jumlah = loadData(words, likelihood, prior, 'bbc-2/tech/*', 'tech'); print "."
    correct += benar
    total += jumlah

    akurasi = correct / total * 100
    print akurasi, "%"
