import pandas
import matplotlib.pyplot as plt
from collections import Counter

namesList = open("names.txt", "r").read().split("\n")

nameStarts = []
for name in namesList:
        nameStarts.append(name[-1])

nameStarts.sort()

letterCounts = Counter(nameStarts)
print(letterCounts)
df = pandas.DataFrame.from_dict(letterCounts, orient="index")

df.plot(kind="bar")
plt.show()