import pygame
from pygame.locals import *

from Joueur import Joueur
from MonBoutton import BouttonImage
from Text import Text


class PlayerName:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre = pygame.display.set_mode((300, 300))
        self.nom = ""
        self.message = Text("Entrez votre nom ", 20, (150, 90), (0, 0, 0))
        self.input = Text("", 20, (150, 120), (255, 0, 0))
        self.background = pygame.image.load("images/game_board.png")
        self.bouton_valider = BouttonImage("images/bouton.png", (150, 205), "valider", )
        self.nomFichier = ""

    def afficher(self):
        # affichage de la dialogue
        user_input = ""
        ecrire = True
        FPS = pygame.time.Clock()
        while ecrire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # definition d'un nom par défaut
                    self.nom = "Joueur"
                    ecrire = False

                elif event.type == pygame.KEYDOWN:
                    # gestion des evenements du clavier
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        if len(user_input) <=5:
                            user_input += event.unicode
                        else:
                            print("Rien a faire")
                    self.message.message = "Entrez votre nom "
                    self.input.message = user_input
                    self.nom = user_input
                    print(self.nom)
                elif pygame.mouse.get_pressed()[0] == 1 :
                    # elif pygame.mouse.get_pressed()[0] == 1 and self.bouton_valider.rect.collidepoint(event.pos):
                    Joueur.nomConfig = self.nom
                    ecrire = False
            FPS.tick(30)
            self.fenetre.blit(self.background, (0, 0))
            self.message.afficher(self.fenetre)
            self.input.afficher(self.fenetre)
            self.bouton_valider.afficher(self.fenetre)
            pygame.display.update()
