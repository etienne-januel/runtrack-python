userInput = int(input("Enter a number below 100: \n"))

if (userInput % 3 == 0) and (userInput % 5 == 0):
  print("FizzBuzz")
else:
  if userInput % 3 == 0:
    print("Fizz")
  elif userInput % 5 == 0:
    print("Buzz")
  else:
    while userInput <= 100:
      print(userInput)
      userInput += 1
    