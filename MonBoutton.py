import pygame
from Text import Text
from pygame.locals import *

class BouttonImage:

    def __init__(self, image, position, message, action=None):

        """
        permet la creation des butons
        :param message: le text a afficher sur le bouton
        :param taille: la taille du text
        :param position: la position du text dans la fenetre sous format de tuple
        :param couleur: la couleur sous format RGB (r, g, b)
        :param couleur_click: la couleur du button lorsque la souris est au dessus d'elle
        :param action: action a effectuer en cas d'appuis sur le bouton
        """
        self.acitver = False
        self.position = position
        self.image = pygame.image.load(image)
        self.action = action
        self.message = Text(message, 25, (position[0] * 2 / 2, position[1] * 2 / 2), (0, 0, 0))
        self.rect = self.image.get_rect()


    def afficher(self, surface):
        self.rect.center = self.position
        # pygame.draw.rect(surface, (255, 0, 0), self.rect, 1) # surface, color, rect, width=0, border_radius=0, border_radius=-1
        surface.blit(self.image, self.rect)
        self.message.afficher(surface)


        # pygame.display.flip()

    # implementation des actions ICI
    def action_execute(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and self.action is not None:
            self.action()




            