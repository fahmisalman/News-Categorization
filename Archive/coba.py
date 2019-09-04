import csv

with open('Train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    words = []
    likelihood = []
    for row in reader:
        words.append(row['words'])
        likelihood.append([float(row['sport']), float(row['business']), float(row['politic']), float(row['entertainment']), float(row['tech'])])
