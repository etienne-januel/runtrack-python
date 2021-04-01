import os, re

parent_dir = os.path.dirname(__file__)

f = open(parent_dir + '/../data.txt', 'r')

data = f.read()

wordSizeOccurency = {}

for word in re.findall(r'\b[a-zA-Z]{1,}\b', data):
  if len(word) in wordSizeOccurency:
    wordSizeOccurency[len(word)] += 1
  else:
    wordSizeOccurency[len(word)] = 1

orderedWordSizeOccurency = dict(sorted(wordSizeOccurency.items()))

print(orderedWordSizeOccurency)

wordSizeOccurencyList = [str(key) for key, val in orderedWordSizeOccurency.items() for _ in range(val)]

import matplotlib.pyplot as plt

plt.title("Occurences de taille de mots")
plt.xlabel('Taille')
plt.ylabel('Total')
plt.hist(wordSizeOccurencyList, bins=len(orderedWordSizeOccurency))

plt.show()