import pygame
from pygame.locals import *

from Joueur import Joueur
from MonBoutton import *
from Music import Music
from Playername import PlayerName
from Text import Text
import sys

from gameState import GameStat

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
orange = (255, 51, 0)
orange_light = (255, 102, 0)
bright_green = (0, 255, 0)

clock = pygame.time.Clock()

class MonMenu:

    def __init__(self, fenetre):
        self.fenDeBase = fenetre
        self.intro_pic = pygame.image.load("image_menu/menu_princ.png")
        self.bt_jouer = BouttonImage("images/bouton.png", (350, 370), "JOUER", self.choixDiff)  #(350, 380) (300, 340)
        #self.bt_inscr = BouttonImage("img/bouton.png", (350, 370), "IDENTITE", self.debuterPartie)  #(350, 380) (300, 340)
        self.bt_fermer = BouttonImage("images/bouton.png", (560, 370), "FERMER",self.destroy)

        self.bt_rejouer = BouttonImage("images/bouton.png", (780, 420), "REJOUER", self.choixDiff)
        self.bt_rejouer_2 = BouttonImage("images/bouton.png", (650, 130), "REJOUER", self.choixDiff)
        self.bt_rejouer_3 = BouttonImage("images/bouton.png", (620, 420), "REJOUER", self.choixDiff)

        self.bt_retour = BouttonImage("icone/back.png", (25, 25), "", self.introGame)
        self.bt_annuler_jeux = BouttonImage("icone/annuler_jeux.png", (25, 75), "", self.introGame)
        self.bt_aide = BouttonImage("icone/aide.png", (25, 25), "", self.foncAbout) #(25, 125)
        self.bt_next = BouttonImage("icone/next.png", (870, 250), "", self.foncAboutNext)
        self.bt_son = BouttonImage("icone/son.png", (850, 25), "",)
        self.bt_pas_son = BouttonImage("icone/pas_son.png", (870, 25), "",)
        #self.bckgrd = pygame.image.load("images/game_board.png")

        self.bckgrd1_about = pygame.image.load("image_menu/about_team.png")
        self.bckgrd2_about = pygame.image.load("image_menu/about_rules.png")
        self.bckgrd_level = pygame.image.load("images/level.png")
        self.bckgrd_vainq = pygame.image.load("images/vainqueur.png")
        self.bckgrd_perd = pygame.image.load("images/perdant.png")

        self.bt_niv1 = BouttonImage("images/bouton.png", (213, 335), "FACILE", self.debuterPartie)
        self.bt_niv1_agr_bas = BouttonImage("images/niveau1.png", (213, 382), "",)
        self.bt_niv1_agr_haut = BouttonImage("images/niveau1.png", (213, 288), "",)

        self.bt_niv2 = BouttonImage("images/bouton.png", (458, 355), "MOYEN", self.debuterPartie)
        self.bt_niv2_agr_bas = BouttonImage("images/niveau2.png", (458, 402), "",)
        self.bt_niv2_agr_haut = BouttonImage("images/niveau2.png", (458, 308), "",)

        self.bt_niv3 = BouttonImage("images/bouton.png", (703, 375), "DIFFICILE", self.debuterPartie)
        self.bt_niv3_agr_bas = BouttonImage("images/niveau3.png", (703, 422), "",)
        self.bt_niv3_agr_haut = BouttonImage("images/niveau3.png", (703, 328), "",)

        self.music = Music()
        self.difficulter = [2, 3, 5]
        self.id_btn = 2

    
    def introGame(self):
        self.music.play_sonIntro()
        continuer = 1
        while continuer:
            self.fenDeBase.blit(self.intro_pic, (0, 0))
            self.bt_jouer.afficher(self.fenDeBase)
            # self.bt_inscr.afficher(self.fenDeBase)
            self.bt_fermer.afficher(self.fenDeBase)
            self.bt_aide.afficher(self.fenDeBase)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_jouer.rect.collidepoint(event.pos):
                        self.bt_jouer.action()
                        continuer = 0
                    if event.button == 1 and self.bt_fermer.rect.collidepoint(event.pos):
                        self.bt_fermer.action()
                        continuer = 0
                    if event.button == 1 and self.bt_aide.rect.collidepoint(event.pos):
                        self.bt_aide.action()
                        continuer = 0
        pygame.quit()

    def destroy(self):
        try:
            pygame.quit()
            sys.exit()
        except SystemExit:
            print("Fermeture du prg")

    def debuterPartie(self):
        # afficher la dialogue pour le nom
        self.music.stop_musique()
        gl = GameStat(None, None, self.fenDeBase, self.id_btn)
        gl.gameLoop()
        if gl.awale.estFinal == True and gl.awale.gagnant == gl.awale.joueur:
            gl.awale.enregistrerStatistiquesJoueur()
            self.foncFinVanq()
        elif gl.awale.estFinal == True and gl.awale.gagnant == gl.awale.CPU:
            # gl.awale.enregistrerStatistiquesJoueur()
            self.foncFinPerd()

        # mettre MATCH NULL
        elif gl.awale.estNul == True:
            gl.awale.enregistrerStatistiquesJoueur()
            self.foncFinNull()
        else:
            self.introGame()
    
    def foncAbout(self):
        continuer = 1
        while continuer:
            self.fenDeBase.blit(self.bckgrd1_about, (0, 0))
            # self.bt_retour.afficher(self.fenDeBase)
            self.bt_next.afficher(self.fenDeBase)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_retour.rect.collidepoint(event.pos):
                        self.bt_retour.action()
                        continuer = 0
                    if event.button == 1 and self.bt_next.rect.collidepoint(event.pos):
                        self.bt_next.action()
                        continuer = 0
    
    def foncAboutNext(self):
        continuer = 1
        while continuer:
            self.fenDeBase.blit(self.bckgrd2_about, (0, 0))
            self.bt_retour.afficher(self.fenDeBase)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_retour.rect.collidepoint(event.pos):
                        self.bt_retour.action()
                        continuer = 0
    
    def foncFinVanq(self):
        continuer = 1
        pygame.mixer.music.set_volume(0.2)
        self.music.play_sonGagne()
        while continuer:
            self.fenDeBase.blit(self.bckgrd_vainq, (0, 0))
            self.bt_rejouer.afficher(self.fenDeBase)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_rejouer.rect.collidepoint(event.pos):
                        self.music.stop_musique()
                        self.music.play_sonIntro()
                        self.bt_rejouer.action()
                        continuer = 0


    def foncFinPerd(self):
        continuer = 1
        self.music.play_sonPerdu()
        while continuer:
            self.fenDeBase.blit(self.bckgrd_perd, (0, 0))
            self.bt_rejouer_2.afficher(self.fenDeBase)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_rejouer_2.rect.collidepoint(event.pos):
                        self.music.stop_musique()
                        self.music.play_sonIntro()
                        self.bt_rejouer_2.action()
                        continuer = 0

    def foncFinNull(self):
        continuer = 1
        self.music.play_sonNull()
        while continuer:
            self.fenDeBase.blit(self.bckgrd_perd, (0, 0))
            self.bt_rejouer_3.afficher(self.fenDeBase)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_rejouer_3.rect.collidepoint(event.pos):
                        self.music.stop_musique()
                        self.music.play_sonIntro()
                        self.bt_rejouer_3.action()
                        continuer = 0

    def entreNom(self):
        playerName = PlayerName(self.fenDeBase)
        playerName.afficher()

    def choixDiff(self):
        # ajout du nom

        self.entreNom()
        self.fenDeBase = pygame.display.set_mode((900, 506))
        continuer = 1
        while continuer:
            self.fenDeBase.blit(self.bckgrd_level, (0, 0))
            self.bt_niv1.afficher(self.fenDeBase)
            self.bt_niv1_agr_bas.afficher(self.fenDeBase)
            #self.bt_niv1_agr_haut.afficher(self.fenDeBase)
            self.bt_niv2.afficher(self.fenDeBase)
            self.bt_niv2_agr_bas.afficher(self.fenDeBase)
            #self.bt_niv2_agr_haut.afficher(self.fenDeBase)
            self.bt_niv3.afficher(self.fenDeBase)
            self.bt_niv3_agr_bas.afficher(self.fenDeBase)
            #self.bt_niv3_agr_haut.afficher(self.fenDeBase)
            self.bt_retour.afficher(self.fenDeBase)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.bt_niv1.rect.collidepoint(event.pos):
                        self.id_btn = self.difficulter[0]
                        self.bt_niv1.action()
                        continuer = 0
                    if event.button == 1 and self.bt_niv2.rect.collidepoint(event.pos):
                        self.id_btn = self.difficulter[1]
                        self.bt_niv2.action()
                        continuer = 0
                    if event.button == 1 and self.bt_niv3.rect.collidepoint(event.pos):
                        self.id_btn = self.difficulter[2]
                        self.bt_niv3.action()
                        continuer = 0
                    if event.button == 1 and self.bt_retour.rect.collidepoint(event.pos):
                        self.bt_retour.action()
                        continuer = 0


