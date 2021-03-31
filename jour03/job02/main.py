import os
import re

parent_dir = os.path.dirname(__file__)

f = open(parent_dir + '/../data.txt', 'r')

data = f.read()

print('Number of occurrences of words :', str(len(re.findall(r'[a-zA-Z]\w+', data))))