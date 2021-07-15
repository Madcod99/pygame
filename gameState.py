import pygame
from pygame.locals import *

from Joueur import Joueur
from MonBoutton import BouttonImage
from Music import Music
from Text import Text
from Trou import Trou
from awale import Awale
from Stat import Stat
from Hand import Hand
from minimax_awale import Minimax

white = (255, 255, 255)
RED = (255, 0, 0)


class GameStat:
    def __init__(self, joueur1, joueur2, fenetre, profondeur):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tablier = pygame.image.load("images/awale_plateau.png")
        self.fond = pygame.image.load("images/game_board.png").convert()
        self.aideMenu = pygame.image.load("image_menu/about_rules.png")
        self.bt_retour = BouttonImage("icone/back.png", (25, 480), "", None)
        self.bt_coupeSon = BouttonImage("icone/pas_son.png", (870, 25), "", None)
        self.bt_retour = BouttonImage("icone/back.png", (25, 480), "", None)
        self.bt_annuler_jeux = BouttonImage("icone/annuler_jeux.png", (75, 480), "", None)
        self.bt_aide = BouttonImage("icone/aide.png", (125, 480), "", None)  # (25, 125)
        self.fenetre = fenetre
        self.listeTrou1 = []
        self.listeTrou2 = []
        self.creation_des_trous()
        self.stat_joueur1 = None
        self.stat_joueur2 = None
        self.HandFPS = 200
        self.handCPU = None
        self.handJoueur = None
        self.sound = Music()
        self.sonJoue = True
        self.profondeurMAX = profondeur
        self.pause = False
        self.nbr = ""
        self.awale = Awale(Joueur.nomConfig)
        self.awale.difficulte = profondeur
        self.latenceJouer = 1200

    def sonEncours(self):

        if self.sonJoue == False:
            self.bt_coupeSon = BouttonImage("icone/pas_son.png", (870, 25), "", None)
            self.bt_coupeSon.afficher(self.fenetre)
        else:
            self.bt_coupeSon = BouttonImage("icone/son.png", (870, 25), "", None)
            self.bt_coupeSon.afficher(self.fenetre)


    def initialise_Hand(self):
        self.handCPU = Hand(self.fenetre, (0, 0), (62, 10), "images/main_CPU.png")
        self.handJoueur = Hand(self.fenetre, (0, 0), (840, 495), "images/main_joueur.png")
        # Hand joueur pos INI (840, 495) pos SIGNI TOUR (840, 450)
        # Hand CPU pos INI (840, 10) pos SIGNI TOUR (840, 55)

    def intialise_stat(self, j1, j2):

        self.stat_joueur1 = Stat(self.fenetre, (450, 450), j1)
        self.stat_joueur2 = Stat(self.fenetre, (450, 50), j2)

    def affiche_stat_joueur(self):

        self.stat_joueur2.afficheStat()
        self.stat_joueur1.afficheStat()

    def creation_des_trous(self):
        # fenetre position color size
        # creation des trous du joueur CPU

        self.listeTrou1.append(Trou(self.fenetre, (196, 200), (255, 0, 0), (50, 50), 4))
        self.listeTrou1.append(Trou(self.fenetre, (298, 200), (255, 0, 0), (50, 50), 4))
        self.listeTrou1.append(Trou(self.fenetre, (400, 197), (255, 0, 0), (50, 50), 4))
        self.listeTrou1.append(Trou(self.fenetre, (504, 197), (255, 0, 0), (50, 50), 4))
        self.listeTrou1.append(Trou(self.fenetre, (605, 198), (255, 0, 0), (50, 50), 4))
        self.listeTrou1.append(Trou(self.fenetre, (705, 200), (255, 0, 0), (50, 50), 4))

        # creation des trous du joueur Joueur

        self.listeTrou2.append(Trou(self.fenetre, (198, 302), (255, 0, 0), (50, 50)))
        self.listeTrou2.append(Trou(self.fenetre, (298, 302), (255, 0, 0), (50, 50)))
        self.listeTrou2.append(Trou(self.fenetre, (400, 299), (255, 0, 0), (50, 50)))
        self.listeTrou2.append(Trou(self.fenetre, (504, 299), (255, 0, 0), (50, 50)))
        self.listeTrou2.append(Trou(self.fenetre, (605, 299), (255, 0, 0), (50, 50)))
        self.listeTrou2.append(Trou(self.fenetre, (705, 299), (255, 0, 0), (50, 50)))

    def afficherTablier(self):

        self.fenetre.blit(self.fond, (0, 0))
        rect = self.tablier.get_rect()
        rect.center = (450, 250)
        self.fenetre.blit(self.tablier, rect)
        # pygame.draw.rect(self.fenetre, RED, rect, 1)

    def afficher_nbr_graine(self):

        nbr_graine = Text(str(self.nbr), 40, (80, 250), (17, 29, 94))
        nbr_graine.afficher(self.fenetre)

    def afficherTrous(self):

        for k in self.listeTrou1:
            k.affiche_valeur()
        for p in self.listeTrou2:
            p.affiche_valeur()

    def afficherMiniMenu(self):
        self.bt_retour.afficher(self.fenetre)
        self.bt_annuler_jeux.afficher(self.fenetre)
        self.bt_aide.afficher(self.fenetre)
        self.bt_coupeSon.afficher(self.fenetre)

        pygame.display.update()
        pygame.time.delay(self.HandFPS)

    def updateTablier(self, awale, player):
        parcours = awale.listeEtats
        parcoursCoordonnees = []
        # liste des coordonnees pour le deplacemenent de la main
        for k in parcours:
            if k == "-":
                print("on doit faire le retour en arriere")
                continue
            elif awale.joueur.nom == k[0]:
                # c'est le joueur on commence par la liste 2
                parcoursCoordonnees.append(self.listeTrou2[k[1]].position)
            elif awale.CPU.nom == k[0]:
                parcoursCoordonnees.append(self.listeTrou1[k[1]].position)

        # c'est a l'affichage du coup d'un joueur
        # print(parcoursCoordonnees)
        # print(parcours)
        if player == awale.joueur:
            # print("ICI")
            # print("[MODIFICATION] listeTrou2")
            j = 0
            playTake = False
            for k in parcours:
                if k[0] == awale.joueur.nom:
                    self.listeTrou2[k[1]].valeur = k[2]
                elif k[0] == "CPU":
                    self.listeTrou1[k[1]].valeur = k[2]

                # affichage de la fenetre de jeu avec le trou changer et play the song
                self.afficherTablier()
                self.afficherTrous()
                self.affiche_stat_joueur()
                # ici on coupe les parcours permier parcours normale dispotion des graines jusqua "-"
                # puis la suite correspond au parcours de bouffe
                if k == "-":
                    playTake = True
                    # self.handJoueur.position_deplacer((840, 450))
                    j= j-1
                    # Hand joueur pos INI (840, 495) pos SIGNI TOUR (840, 450)
                if playTake:
                    self.sound.play_takeGraine()
                else: 
                    self.sound.play_dropGraine()

                self.handCPU.positionInitial()
                self.handJoueur.position_deplacer(parcoursCoordonnees[j])
                # affichage du mini menu
                self.afficherMiniMenu()
                j += 1

        elif player == awale.CPU:
            print("[MODIFICATION] listeTrou1")
            it = 0
            playTake = False
            for k in parcours:
                if k[0] == awale.joueur.nom:
                    # self.listeTrou2[k[1]].valeur = awale.joueur.cases[k[1]]
                    self.listeTrou2[k[1]].valeur = k[2]

                elif k[0] == "CPU":
                    # self.listeTrou1[k[1]].valeur = awale.CPU.cases[k[1]]
                    self.listeTrou1[k[1]].valeur = k[2]
                else:
                    print("Nothing to do")
                # Affichage de la fenetre de jeu avec le trou changer
                self.afficherTablier()
                self.afficherTrous()
                self.affiche_stat_joueur()

                # ici on coupe les parcours permier parcours normale dispotion des graines jusqua "-"
                # puis la suite correspond au parcours de bouffe
                if k == "-":
                    playTake = True
                    # self.handCPU.position_deplacer((62, 52))
                    it = it -1
                    # Hand CPU pos INI (840, 10) pos SIGNI TOUR (840, 55)
                if playTake:
                    self.sound.play_takeGraine()
                else:
                    self.sound.play_dropGraine()
                self.handJoueur.positionInitial()
                self.handCPU.position_deplacer(parcoursCoordonnees[it])
                # Affichage du mini menu
                self.afficherMiniMenu()
                it += 1

        else:
            for k in range(6):
                self.listeTrou2[k].valeur = awale.joueur.cases[k]
                self.listeTrou1[k].valeur = awale.CPU.cases[k]

    def gamePause(self, pause):
        pause = True
        while pause:
            for event in pygame.event.get():
                if (event.type == QUIT):
                    pause = False
                if self.bt_retour.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                    pause = False
            self.fenetre.blit(self.aideMenu, (0, 0))
            self.bt_retour.afficher(self.fenetre)

            pygame.display.update()

    def cpuIAjoue(self, awale):
        m = Minimax(awale, awale.CPU, awale.CPU, None)
        return awale.parseOut(m.indexMinimax())

    def gestionClickMenu(self):
        #si click gauche
        if pygame.mouse.get_pressed()[0] == 1:
            if self.bt_coupeSon.rect.collidepoint(pygame.mouse.get_pos()):
                if self.sonJoue:
                    self.sound.stop_musique()
                    self.sonJoue = False
                else:
                    self.sound.play_sonDeFond()
                    self.sonJoue = True
            #quitter le jeu et partir au menu principal
            if self.bt_retour.rect.collidepoint(pygame.mouse.get_pos()):
                self.awale.estFinal = True
                partieEncours = False
            # mettre le jeu en pause en creant une boucle infini ici
            if self.bt_aide.rect.collidepoint(pygame.mouse.get_pos()):
                self.gamePause(self.pause)
                if self.pause == False:
                    print("sortie de pause")
            # etat prec
            if self.bt_annuler_jeux .rect.collidepoint(pygame.mouse.get_pos()) and self.bt_annuler_jeux.acitver == True:
                # afficher l'etat précedant le coup jouer
                self.bt_annuler_jeux.acitver = False
                self.awale = self.awale.retourSurPrecedent()
                self.awale = self.awale.retourSurPrecedent()
                self.stat_joueur1.statJoueur = self.awale.joueur
                self.stat_joueur2.statJoueur = self.awale.CPU

        # affichage du nombre de graine
        if pygame.mouse.get_pressed()[2] == 1:
            for l1 in self.listeTrou1:
                if l1.rect.collidepoint(pygame.mouse.get_pos()):
                    self.nbr = l1.valeur
            for l2 in self.listeTrou2:
                if l2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.nbr = l2.valeur

    def affichageDeBase(self):
        self.afficherTablier()
        self.afficherTrous()
        self.updateTablier(self.awale, None)
        if (self.awale.tourJoueur == self.awale.joueur):
            self.handJoueur.position_deplacer((840, 450))
            self.handCPU.positionInitial()
            # attendre que le joueur joue
        else:
            self.handCPU.position_deplacer((62, 52))
            self.handJoueur.positionInitial()
        self.affiche_stat_joueur()
        self.afficher_nbr_graine()
        self.bt_retour.afficher(self.fenetre)
        self.bt_annuler_jeux.afficher(self.fenetre)
        self.bt_aide.afficher(self.fenetre)
        self.sonEncours()
        pygame.display.update()

    def gameLoop(self):
        self.sound.play_sonDeFond()
        self.intialise_stat(self.awale.joueur, self.awale.CPU)
        self.initialise_Hand()
        self.pause = False
         # nbr => Affichage du nombre de graines d"une case
        self.awale.tourJoueur = self.awale.joueur
        playing = False
        partieEncours = False
        while not self.awale.estFinal:
            # afficher le nbr de graine en survole
            # IA doit joueur ici
            if (self.awale.tourJoueur == self.awale.CPU):
                # print("IA play")
                playing = True
                self.awale.CPUJoue(self.cpuIAjoue(self.awale))
            # attente de click sur listeTrou2 pour que le joueur joue
            for event in pygame.event.get():
                if event.type == QUIT:
                    partieEncours = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # print("Joueur play")
                    # event click du joueur
                    if pygame.mouse.get_pressed()[0] == 1:
                        for k in self.listeTrou2:
                            if self.awale.tourJoueur == self.awale.joueur and k.rect.collidepoint(pygame.mouse.get_pos()):
                                # print(self.awale.tourReussira)
                                case = self.listeTrou2.index(k)
                                if self.awale.joueur.cases[case] != 0:
                                    self.sound.play_takeGraine()
                                    playing = True
                                    self.awale.joueurJoue(case + 1)
                    # gestion des events dans gestionClickMenu
                    self.gestionClickMenu()

            if self.awale.tourJoueur == self.awale.CPU and playing == True and self.awale.tourReussi == True:
                # affichage lors du coup de CPU
                self.bt_annuler_jeux.acitver = True
                playing = False
                self.updateTablier(self.awale, self.awale.CPU)
                self.nbr = ""
                self.awale.tourJoueur = self.awale.joueur

            elif self.awale.tourJoueur == self.awale.joueur and playing == True and self.awale.tourReussi == True:
                # affichage lors du coup de Joueur
                playing = False
                self.updateTablier(self.awale, self.awale.joueur)
                self.nbr = ""
                self.awale.tourJoueur = self.awale.CPU
                self.affichageDeBase()
                pygame.display.update()
                pygame.time.delay(self.latenceJouer)
            else:
                # affichage de base
                self.affichageDeBase()
                self.awale.tourJoueur = self.awale.joueur


        self.sound.stop_musique()



