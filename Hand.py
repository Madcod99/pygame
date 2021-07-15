import pygame


class Hand:
    def __init__(self, fenetre, position_deplace, position_initial, image):

        """
        creation d'une main
        :param fenetre: fenetre de base du jeu
        :param position_deplace: la positon souhaitée
        :param position_initial: la position initial apres deplacement de la main enfin c'est comme un retour au source
        :param image: l'image de la main, fournir le chemin de la main
        """

        self.fen = fenetre
        self.position_deplace = position_deplace
        self.position_initial = position_initial
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def affiche(self):
        # rect = self.image.get_rect()
        # rect.center = self.position_deplace
        # self.rect = rect
        self.fen.blit(self.image, self.rect)
        # pygame.draw.rect(self.fen, (255, 0, 0), self.rect, 1)


    def positionInitial(self):
        rect = self.image.get_rect()
        rect.center = self.position_initial
        self.rect = rect

        self.affiche()

    def moving(self, position):
        self.rect.move_ip(position)

    def position_deplacer(self, position):
        rect = self.image.get_rect()
        self.position_deplace = position
        rect.center = self.position_deplace
        self.rect = rect
        self.affiche()


