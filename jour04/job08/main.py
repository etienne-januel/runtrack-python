# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases.
# Placez sur ce plateau n dames de manière à ce qu’aucune dame ne puisse
# se “prendre”, quand cela est possible. La valeur de n est renseignée par
# l’utilisateur. Quand cela est possible, le programme devra afficher dans le
# terminal le plateau de jeu avec le caractère ‘O’ pour les cases vides et le
# caractère ‘X’ pour représenter les dames.

import numpy as np
import random

emptyBox = 'O'

class ChessQueen:
  def __init__(self, width):
    self.width = width
    self.board = self.genBoard(width)
    
  def genBoard(self, n):
    board = [['O'] * n ] * n
    return board

  def printBoard(self, i = 0):
    # print(self.board)
    for x in self.board:
      print(*x)
    # print(self.board[3])
    # if i < len(self.board):
    #   print(self.board[i])
    #   return self.printBoard(i + 1)

  def placeQueens(self):
    self.board[2][5] = 'A'
    # x = random.randint(0, self.width - 1)
    # y = random.randint(0, self.width - 1)
    # if self.board[y][x]


# boardWidth = int(input('Veuillez choisir la taille du plateau: '))
boardWidth = 8

chess = ChessQueen(boardWidth)
chess.placeQueens()
chess.printBoard()
