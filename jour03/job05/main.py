import os
import re

parent_dir = os.path.dirname(__file__)

f = open(parent_dir + '/../data.txt', 'r')

data = f.read()

alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

for char in re.findall(r'[a-zA-Z]', data):
  alphabet[char.upper()] += 1

listAlphabet = [key for key, val in alphabet.items() for _ in range(val)]

import matplotlib.pyplot as plt

plt.title("Occurences de lettres")
plt.xlabel('Lettres')
plt.ylabel('Total')
plt.hist(listAlphabet, bins=26)

plt.show()