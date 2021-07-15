import pygame
class Text:
    def __init__(self, message, taille, position, couleur):

        """"permet d'afficher du text sur une surface
            :param message : le message a afficher
            :param taille :  taille du text integer
            :param position : tuple (x, y)
            :param couleur : couleur de valeur RGB (0,0,0) noir par exmple"""

        self.message = message
        self.taille = taille
        self.position = position
        self.couleur = couleur

    def afficher(self, surface):

        textFont = pygame.font.Font('police/outofafrica.ttf', self.taille)
        textSurface = textFont.render(self.message, True, self.couleur)
        textRect = textSurface.get_rect()
        textRect.center = self.position
        surface.blit(textSurface, textRect)




