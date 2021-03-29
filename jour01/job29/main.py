height = int(input("Enter a height: \n"))

x = 1
y = 1

while y <= height:
  tempLine = ''
  w = height - y
  while w > 0:
    tempLine += ' '
    w -= 1

  # while x <= height:
  if y == 1:
    tempLine += '/\\'
  else:
    tempLine += '/'
    z = y + y - 2
    while z > 0:
      if y == height:
        tempLine += '_'
      else:
        tempLine += ' '
      z -= 1
    tempLine += '\\'
    # x += 1
    # print(tempLine)


  print(tempLine)
  x = 1
  y += 1
