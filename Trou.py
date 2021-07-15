import pygame

from Text import Text


class Trou:
    def __init__(self, surface, position, couleur, taille, valeur=4):
        """
        class permettant de creer des trous sur le tablier
        :param surface: surface sur laquelle on veut mettre le trou
        :param position: la positon donnée sous forme de tuple (10, 20) exmple
        :param couleur: la couleur du trou donné sous format RGB (0,0,0) noir par exmple
        :param taille: la taille du trou
        :param valeur: afficher le nombre de graine dans un trou
        """

        self.surface = surface
        self.position = position
        self.couleur = couleur  # (255, 2, 6) sous forme de rgb
        self.size = taille
        # self.image = pygame.transform.scale(pygame.image.load("image/circle.png").convert(), self.size)
        # self.rect = self.image.get_rect()
        self.valeur = valeur
        self.liste_trounum=  ["Trou0.png", "Trou1.png", "Trou2.png", "Trou3.png", "Trou4.png", "Trou5.png", "Trou6.png", "Trou7.png"
                              ,"Trou8.png", "Trou9.png", "Trou10.png", "Trou11.png", "Trou12.png", "Trou13.png", "Trou14.png", "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png"
                              , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" , "Trou15.png" ]
        self.liste_trou_charger = []
        self.rect = self.position
        self.load_images()
        self.activer = True


    def load_images(self):
        for k in self.liste_trounum:
            tt = pygame.image.load("images/"+k)
            self.liste_trou_charger.append(tt)
            # self.liste_rect.append(tt.get_rect)


    def affiche_valeur(self):
        #val = Text(str(self.valeur), 20, (self.rect.x + 25, self.rect.y + 25), (52, 61, 235))
        # val.afficher(self.surface)
        # affiche directement la valeur du trou correspondant

        for l in range(len(self.liste_trou_charger)):
            if l == self.valeur:
                rect = self.liste_trou_charger[l].get_rect()
                rect.center = self.position
                # print(rect)
                # rect du trou actif
                self.rect = rect
                # self.rect = rect
                self.surface.blit(self.liste_trou_charger[l], (rect.x, rect.y))
                # pygame.draw.rect(self.surface, (255, 0, 0), rect, 1)



