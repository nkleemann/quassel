import pandas
import matplotlib.pyplot as plt
from collections import Counter

namesList = open("names.txt", "r").read().split("\n")

names = []
for name in namesList:
    for c in name:
        names.append(c.lower())

names.sort()
letterCounts = Counter(names)

df = pandas.DataFrame.from_dict(letterCounts, orient="index")

df.plot(kind="bar")
plt.show()