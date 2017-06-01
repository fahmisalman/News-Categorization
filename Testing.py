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
    x = '''West End to honour finest shows

The West End is honouring its finest stars and shows at the Evening Standard Theatre Awards in London on Monday.

The Producers, starring Nathan Lane and Lee Evans, is up for best musical at the ceremony at the National Theatre. It is competing against Sweeney Todd and A Funny Thing Happened on the Way to the Forum for the award. The Goat or Who is Sylvia? by Edward Albee, The Pillowman by Martin McDonagh and Alan Bennett's The History Boys are shortlisted in the best play category.

Pam Ferris, Victoria Hamilton and Kelly Reilly are nominated for best actress. Ferris - best known for her television roles in programmes such as The Darling Buds of May - has made the shortlist for her role in Notes on Falling Leaves, at the Royal Court Theatre. Meanwhile, Richard Griffiths, who plays Hector in The History Boys at the National Theatre, will battle it out for the best actor award with Douglas Hodge (Dumb Show) and Stanley Townsend (Shining City). The best director shortlist includes Luc Bondy for Cruel and Tender, Simon McBurney for Measure for Measure, and Rufus Norris for Festen.

Festen is also shortlisted in the best designer category where Ian MacNeil, Jean Kalman and Paul Arditti will be up against Hildegard Bechtler, for Iphigenia at Aulis, and Paul Brown, for False Servant. The Milton Shulman Award for outstanding newcomer will be presented to Dominic Cooper (His Dark Materials and The History Boys), Romola Garai (Calico), Eddie Redmayne (The Goat, or Who is Sylvia?) or Ben Wishaw (Hamlet). And playwrights David Eldridge, Rebecca Lenkiewicz and Owen McCafferty will fight it out for The Charles Wintour Award and a 30,000 bursary. Three 50th Anniversary Special Awards will also be presented to an institution, a playwright and an individual.
'''
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