import pygame
import sys
from pygame.locals import *

GREY = (128, 128, 128)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

tikTakToe = pygame
tikTakToe.init()

tikTakToe.display.set_caption("TikTakToe")
tikTakToeDisplay = pygame.display.set_mode((600,600))
tikTakToeDisplay.fill(WHITE)

tikTakToe.draw.line(tikTakToeDisplay, RED, (0, 200), (600, 200))
tikTakToe.draw.line(tikTakToeDisplay, RED, (0, 400), (600, 400))
tikTakToe.draw.line(tikTakToeDisplay, RED, (200, 0), (200, 600))
tikTakToe.draw.line(tikTakToeDisplay, RED, (400, 0), (400, 600))

while True:
    tikTakToe.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()