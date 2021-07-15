from MonMenu import MonMenu
import pygame as py

 
py.init()
py.display.set_caption("Le jeu d'Awale 2.0 ")
fen = py.display.set_mode((900, 506))

menu = MonMenu(fen)
menu.introGame()

# TODO
#  1 implement alpha beta / ok *****
#  2 deplacement de la main sur chque trou / ok******
#  3 maintient clique droit affiche nbr de graine ok*****
#  4 about règles et info dev ok *****
#  ------------------------------
#  2 fonction retour etat precedent (bien jouer) # LOGIQUE ET BTN ok*****
#  3 deplacement sequenciel de la main (Utilisation de la liste etat)  OK****
#  4 son deplacement de main ok*****
#  5 mise des regles (determination gagner perdre, bouffe tous, probleme de symetrie)
#  6 son background ok****
#  7 interface niveau facile normal difficile modifier le fichier awale
#  8 passage de tour OK******
#  11 stat en fonction de chaque joueur sous forme d'histogramme (Matplotlib) ok **** reste integration
#  12 couper la musique ok****
#  13 interface gagne ou perdue ok ******
#  14 [DDK] Ajouter une interface d'affichage de statistiques







