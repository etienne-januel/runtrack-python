import os
import re

parent_dir = os.path.dirname(__file__)

domains = ['.com', '.net', '']

f = open(parent_dir + '/../domains.xml', 'r')

data = f.read()

print('Number of occurrences of domains :', str(len(re.findall(r'([.][a-z]{2,6})\W', data))))