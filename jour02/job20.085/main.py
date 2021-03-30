class bcolors:
  YELLOW = '\033[93m'
  RED = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  
caseVide = bcolors.BOLD + ' O '
caseJaune = bcolors.BOLD + bcolors.YELLOW + ' J ' + bcolors.ENDC
caseRouge = bcolors.BOLD + bcolors.RED + ' R ' + bcolors.ENDC

class Board: 
  def __init__(self, width: int, height: int):
    self.width = width #Largeur
    self.height = height #Hauteur
    self.plateau = []

    # ligne = []
    # while width > 0:
    #   ligne.append(caseVide)
    #   width -= 1

    # while height > 0:
    #   self.plateau.append(ligne)
    #   height -= 1

    row = self.height
    while row > 0:
      column = self.width
      ligne = []
      while column > 0:
        ligne.append(caseVide)
        column -= 1
      self.plateau.append(ligne)
      row -= 1
      
  
  def afficherPlateau(self):
    # # print(self.plateau)
    # for ligne in self.plateau:
    #   print(ligne)
    for ligne in self.plateau:
      ligneTemp = ''
      for case in ligne:
        ligneTemp += case
      print(ligneTemp)
      
  
  def play(self, columnIndex: int, activePlayer: str):
    if columnIndex <= self.width and columnIndex > 0:
      # print('debug')
      # print(self.plateau[5][columnIndex - 1])
      # self.plateau[5][columnIndex - 1] = caseJaune
      rowIndex = self.height - 1
      while rowIndex >= 0:
        if self.plateau[rowIndex][columnIndex - 1] == caseVide:
          if activePlayer == 'Jaune':
            self.plateau[rowIndex][columnIndex - 1] = caseJaune
          elif activePlayer == 'Rouge':
            self.plateau[rowIndex][columnIndex - 1] = caseRouge
          
          return True
        rowIndex -= 1
      return False

  def isThereAWinner(self):
    # Looking From Bottom-Right To Top-Right Horizontally
    row = self.height - 1
    while row > 0:
      column = self.width - 1
      while column > 0:
        activeColor = self.plateau[row][column]
        # Horizontal
        if self.plateau[row][column] != caseVide: 
          if self.plateau[row][column] == activeColor and self.plateau[row][column - 1] == activeColor and self.plateau[row][column - 2] == activeColor and self.plateau[row][column - 3] == activeColor:
            return activeColor
          # # Vertical
          if self.plateau[row][column] == activeColor and self.plateau[row - 1][column] == activeColor and self.plateau[row - 2][column] == activeColor and self.plateau[row - 3][column] == activeColor:
            return activeColor
          # Horizontals
          if column >= 3 and row >= 3:
            if self.plateau[row][column] == activeColor and self.plateau[row - 1][column - 1] == activeColor and self.plateau[row - 2][column - 2] == activeColor and self.plateau[row - 3][column - 3] == activeColor:
              return activeColor
          # Right To Left
          if column <= (self.width - 4) and row >= 3:
            if self.plateau[row][column] == activeColor and self.plateau[row - 1][column + 1] == activeColor and self.plateau[row - 2][column + 2] == activeColor and self.plateau[row - 3][column + 3] == activeColor:
              return activeColor

        column -= 1
      row -= 1
    return False


def game():
  width = int(input('\nChoisissez une largeur: '))
  height = int(input('\nChoisissez une hauteur: '))

  PuissanceQuatro = Board(width, height)
  print('\n')
  PuissanceQuatro.afficherPlateau()

  nbTour = 0
  while PuissanceQuatro.isThereAWinner() != caseJaune and PuissanceQuatro.isThereAWinner() != caseRouge:
    activePlayer = 'Jaune' if nbTour % 2 == 0 else 'Rouge'
    print('\nC\'est au joueur ' + activePlayer + ' de jouer !\n')
    column = int(input('Choisissez une colonne ou placer votre pion:(0..' + str(width) + ') '))
    if column != '' and column > 0 and column <= width:
      print('\n')
      if PuissanceQuatro.play(column, activePlayer):
        PuissanceQuatro.afficherPlateau()
        nbTour += 1
      else:
        print('Cette colonne est déjà remplie !')

  print('WINNER WINNER CHICKEN DINNER')
  print('Le joueur ' + ('Jaune' if PuissanceQuatro.isThereAWinner() == caseJaune else 'Rouge' ) + ' à gagné !')
game()