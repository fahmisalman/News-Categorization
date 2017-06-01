import csv

z = [['a', 'b', 'c']]
a = [[1.2,'abc',3],[1.2,'werew',4],[1.4,'qew',2]]
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(z)
    writer.writerows(a)

