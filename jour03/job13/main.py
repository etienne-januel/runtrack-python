import os, re

parent_dir = os.path.dirname(__file__)

f = open(parent_dir + '/../data.txt', 'r')

data = f.read()

alphabetFirstLetterOccurency = {}

for char in re.findall(r'\b[a-zA-Z]', data):

  if char.upper() in alphabetFirstLetterOccurency:
    alphabetFirstLetterOccurency[char.upper()] += 1
  else:
    alphabetFirstLetterOccurency[char.upper()] = 1

orderedAlphabetFirstLetterOccurency = dict(sorted(alphabetFirstLetterOccurency.items()))

alphabetFirstLetterOccurencyList = [str(key) for key, val in orderedAlphabetFirstLetterOccurency.items() for _ in range(val)]

import matplotlib.pyplot as plt

plt.title("Occurences de Premières lettres")
plt.xlabel('Lettres')
plt.ylabel('Total')
plt.hist(alphabetFirstLetterOccurencyList, bins=len(alphabetFirstLetterOccurency))

plt.show()