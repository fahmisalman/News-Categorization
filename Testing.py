import csv
import Preprocessing
import re
import math


def loadDataTrain():
    with open("Likelihood.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        words = []
        likelihood = []
        for row in reader:
            words.append(row['words'])
            likelihood.append([float(row['sport']), float(row['business']), float(row['politic']), float(row['entertainment']), float(row['tech'])])
    csvfile.close
    with open("Prior.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        prior = []
        for row in reader:
            prior.append(float(row['prior']))
    csvfile.close
    return words, likelihood, prior


if __name__ == '__main__':
    words, likelihood, prior = loadDataTrain()
    pre = Preprocessing.Preprocessing()
    x = '''[ENTERTAIMENT]

Gallery unveils interactive tree

A Christmas tree that can receive text messages has been unveiled at London's Tate Britain art gallery.

The spruce has an antenna which can receive Bluetooth texts sent by visitors to the Tate. The messages will be "unwrapped" by sculptor Richard Wentworth, who is responsible for decorating the tree with broken plates and light bulbs. It is the 17th year that the gallery has invited an artist to dress their Christmas tree. Artists who have decorated the Tate tree in previous years include Tracey Emin in 2002.

The plain green Norway spruce is displayed in the gallery's foyer. Its light bulb adornments are dimmed, ordinary domestic ones joined together with string. The plates decorating the branches will be auctioned off for the children's charity ArtWorks. Wentworth worked as an assistant to sculptor Henry Moore in the late 1960s. His reputation as a sculptor grew in the 1980s, while he has been one of the most influential teachers during the last two decades. Wentworth is also known for his photography of mundane, everyday subjects such as a cigarette packet jammed under the wonky leg of a table.
'''
    x = x.lower()
    x = re.sub(r'[^a-z]', ' ', x)
    x = pre.tokenisasi(x)
    x = pre.stopwordRemoval(x)
    x = pre.lemmatization(x)
    # print x
    probs = []
    for j in range(len(prior)):
        tmp = 1
        for i in range(len(x)):
            if x[i] in words:
                # print x[i]
                # print tmp
                temp = words.index(x[i])
                tmp *= math.log(likelihood[temp][j])
        tmp *= prior[j]
        probs.append(tmp)
    # print probs
    # probs.sort(reverse=True)
    # print probs
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
    # print words
    # print likelihood
    # print prior
