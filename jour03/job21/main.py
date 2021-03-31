
#TODO: Pas Fini
import os, re

parent_dir = os.path.dirname(__file__)

f = open(parent_dir + '/../data.txt', 'r')

data = f.read()

alphabetFirstLetterAfterLettterOccurency = {}

dataBig = re.findall(r'\b[a-zA-Z]', data)

for index, char in enumerate(dataBig, start=1):
  if index + 1 < len(dataBig):
    if char.upper() in alphabetFirstLetterAfterLettterOccurency:
      if dataBig[index + 1] in alphabetFirstLetterAfterLettterOccurency[char.upper()]:
        alphabetFirstLetterAfterLettterOccurency[char.upper()][dataBig[index + 1].upper()] += 1
      else:
        alphabetFirstLetterAfterLettterOccurency[char.upper()][dataBig[index + 1].upper()] = 1
    else:
      alphabetFirstLetterAfterLettterOccurency[char.upper()] = {}
      alphabetFirstLetterAfterLettterOccurency[char.upper()][dataBig[index + 1].upper()] = 1

orderedAlphabetFirstLetterAfterLettterOccurency = dict(sorted(alphabetFirstLetterAfterLettterOccurency.items()))

tempOrderedAlphabetFirstLetterAfterLettterOccurency = {}
for key, val in orderedAlphabetFirstLetterAfterLettterOccurency.items():
  tempOrderedAlphabetFirstLetterAfterLettterOccurency[key] = dict(sorted(val.items()))

orderedAlphabetFirstLetterAfterLettterOccurency = tempOrderedAlphabetFirstLetterAfterLettterOccurency

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(10)

# for key, val in orderedAlphabetFirstLetterAfterLettterOccurency.items():
  # plt.plot(val.items(), key)
  # plt.plot(x, 2 * x)
  # plt.plot(x, 3 * x)
  # plt.plot(x, 4 * x)

# plt.legend(['y = x', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')

# plt.show()
