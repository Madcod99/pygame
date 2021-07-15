import pygame
from Text import Text


class Stat:
    def __init__(self, fen, position, statjoueur):
        """
        afficher les stats de chaque joueurs nombre de graine gagné
        """
        self.surface = fen
        self.statJoueur = statjoueur # l'objet joueur doit etre ici
        self.image_stat = pygame.image.load("images/bouton.png")
        self.position = position
        self.rect = self.image_stat.get_rect()

    def afficheStat(self):
        # initialiser la police ici qui dreva contenir le score du joueur*
        nom = str(self.statJoueur.nom)
        score = nom + " "+ str(self.statJoueur.grainesGagnees)
        score_print = Text(score, 20, self.position, (0, 0, 0))
        rect = self.image_stat.get_rect()
        rect.center = self.position
        self.rect = rect
        self.surface.blit(self.image_stat, rect)
        score_print.afficher(self.surface)
        # pygame.draw.rect(self.surface, (255, 0, 0), rect, 1)


