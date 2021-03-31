import os
parent_dir = os.path.dirname(__file__)

userInput = str(input('Kesta ? '))

f = open(parent_dir + '/output.txt', 'w')
f.write(userInput)

f = open(parent_dir + '/output.txt', 'r')
print(f.read())
f.close()


