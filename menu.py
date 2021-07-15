import pygame
from pygame.locals import *
from Button import Button
from Text import Text
from gameState import GameStat

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)

clock = pygame.time.Clock()

class Menu:

    def __init__(self, fenetre):
        self.fenDeBase = fenetre
        self.couleur = white
        self.awale_img = pygame.image.load("images/menu_princ.png")
        self.btn_jouer = Button("Jouer", (100, 50), (300, 350), red, bright_red, self.choixTypeJeu)
        self.btn_quitter = Button("Quitter", (100, 50), (500, 350), green, bright_green, self.destroy)
        self.btn_vs_ia = Button("Jouer contre l'IA", (200, 50), (350, 150), red, bright_red, self.lance_jeu)
        self.btn_vs_humain = Button("Jouer à deux", (200, 50), (350, 250), red, bright_red, self.lance_jeu)
        self.titre = Text("Jeu d'awalé 2.0", 30, (450, 50), black)


    def introGame(self):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    break
            # if pygame.mouse.get_pressed()[0] == 1:
            #     self.btn_vs_humain.action()
            # if pygame.mouse.get_pressed()[0] == 1:
            #     self.btn_vs_ia.action()

            self.fenDeBase.fill(self.couleur)
            self.fenDeBase.blit(self.awale_img, (0, 0))
            self.btn_jouer.afficher(self.fenDeBase)
            self.btn_quitter.afficher(self.fenDeBase)
            self.titre.afficher(self.fenDeBase)

            pygame.display.flip()

    def choixTypeJeu(self):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    break

            if pygame.mouse.get_pressed()[0] == 1:
                if self.btn_vs_humain.action is None:
                    self.btn_vs_humain.action()
            if pygame.mouse.get_pressed()[0] == 1:
                if self.btn_vs_ia.action is None:
                    self.btn_vs_ia.action()

            #jouer a deux ou contre l'algo Bête
            self.fenDeBase.fill(self.couleur)
            self.titre.afficher(self.fenDeBase)
            self.btn_vs_ia.afficher(self.fenDeBase)
            self.btn_vs_humain.afficher(self.fenDeBase)

            pygame.display.flip()


    def destroy(self):
        pygame.quit()
        quit()

    def lance_jeu(self):
        gl = GameStat(None, None, self.fenDeBase)
        print("GAME LOOP")
        # gl.gameLoop()



