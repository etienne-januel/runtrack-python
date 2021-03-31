import os
import re

parent_dir = os.path.dirname(__file__)

f = open(parent_dir + '/../data.txt', 'r')

data = f.read()

userInput = str(input('Choisisez un nombre: '))

print('Number of occurrences of words :', str(len(re.findall(r'\b[a-zA-Z]{' + userInput + r'}\b', data))))