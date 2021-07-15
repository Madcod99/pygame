import pygame
from pygame.locals import *
from MonBoutton import *
from MonMenu import *

pygame.init()
pygame.font.init()

fen = pygame.display.set_mode((900, 506))

menu = MonMenu(fen)
menu.introGame()

