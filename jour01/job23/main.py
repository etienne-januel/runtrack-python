width = int(input("Enter a width: \n"))
height = int(input("Enter a height: \n"))

x = 1
y = 1

while y <= height:
  tempLine = ''
  while x <= width:
    if x == 1 or x == width:
      tempLine += '|'
    else:
      tempLine += '-'

    x += 1

  print(tempLine)
  x = 1
  y += 1
