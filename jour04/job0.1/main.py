def recursive(x):
  if x == 1:
    return 1
  else:
    return (x * recursive(x-1))


userInput = int(input('Quel factoriel voulez vous calculer: '))
print("Le factoriel de ", userInput, " est ", recursive(userInput))