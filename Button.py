import pygame
from pygame.locals import *
from Text import Text


class Button:

    def __init__(self, message, taille, position, couleur=None, couleur_click=None, action=None):
        """
        permet la creation des butons
        :param message: le text à afficher sur le bouton
        :param taille: la taille du text
        :param position: la position du text dans la fenetre sous format de tuple
        :param couleur: la couleur sous format RGB (r, g, b)
        :param couleur_click: la couleur du button lorsque la souris est au dessus d'elle
        :param action: action à effectuer en cas d'appuis sur le bouton
        :param btn_image: image en arriere plan
        """

        self.taille = taille
        self.position = position
        self.couleur = couleur
        self.couleur_click = couleur_click
        self.action = action
        self.message = Text(message, 20, (position[0] + taille[0] / 2, position[1] + taille[1] / 2), (0, 0, 0))
        self.btn_image = pygame.image.load("images/bouton.png")
        self.rect = self.btn_image.get_rect()
        self.rect.center = self.position


    def afficher(self, surface):

        # implementation du texte
        message = Text(self.message, (10, 10), (self.rect.x, self.rect.y), (0, 0, 0))
        surface.blit(self.btn_image, self.rect)
        pygame.draw.rect(surface, self.couleur, self.rect, 1)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print("click sur bouton")
                    self.action_execute()
        message.afficher(self.rect)


    # implementation des actions ICI

    def action_execute(self):
        click = pygame.mouse.get_pressed()
        print(click)
        if click[0] == 1 and self.action is not None:
            print("Inside boucle")
            self.action()
