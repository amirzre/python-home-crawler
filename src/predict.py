import csv
from sklearn import tree


x = []
y = []

with open("fixtures/data/data.csv", 'r') as f:
    data = csv.reader(f)
    for line in data:
        x.append(line[5:9])
        y.append(line[9])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[4, 2, 250, 65000000], [2, 2, 550, 120000000]]
answer = clf.predict(new_data)
print(answer)
