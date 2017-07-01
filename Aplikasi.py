import Preprocessing
import math
import csv


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


if __name__ == '__main__':

    words, likelihood, prior = loadDataTrain()

    pre = Preprocessing.Preprocessing()
    x = '''West End to honour finest shows'''
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
        print "sport"
    elif higher[0] == 1:
        print "business"
    elif higher[0] == 2:
        print "politic"
    elif higher[0] == 3:
        print "entertainment"
    elif higher[0] == 4:
        print "tech"