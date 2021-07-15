from Joueur import Joueur
from copy import deepcopy
# import statistiques

class Awale:
    def __init__(self, nom_joueur : str):
        self.nombreCasesJoueur = 6

        self.casesJoueur = [4] * self.nombreCasesJoueur
        self.casesCPU = [4] * self.nombreCasesJoueur
        self.joueur = Joueur(nom_joueur.upper(), self.casesJoueur)
        self.CPU = Joueur("CPU", self.casesCPU)
        self.difficulte = None

        self.tourJoueur = None  # Type Joueur
        self.tourReussi = True
        self.listeEtats = []

        self.estFinal = False
        self.gagnant = None
        self.perdant = None

        self.estNul = None

        self.compteurJeuSymetrique = 0
        self.estSymetrique = False

        self.etatPrecedent = self

    def joueurJoue(self, case):
        case = self.parseIn(case)
        self.jouerTourSurCase(case, self.joueur)

    def CPUJoue(self, case):
        case = self.parseIn(case)
        self.jouerTourSurCase(case, self.CPU)

    def jouerTourSurCase(self, case, joueur):
        self.listeEtats = []
        precedent = deepcopy(self)

        adversaire = self.joueur if joueur is self.CPU else self.CPU

        if not self.tourJouable(case, joueur, adversaire):
            print("Cases adversaires vide ! Maudit là joue ailleurs")
            self.listeEtats = []
            self.tourReussi = False
            return

        # Configuration des variables distribution
        changementDeCamp = False
        camp = joueur
        grainesEnMain = joueur.cases[case]
        joueur.cases[case] = 0
        caseCourante = case + 1 if joueur is self.joueur else case - 1
        derniereCase = caseCourante
        
        self.listeEtats.append((joueur.nom, case, 0))

        # Vérification de la faisabilité du tour
        if not grainesEnMain:
            print("On peut pas jouer ici orh !")
            self.listeEtats = []
            self.tourReussi = False
            return

        self.listeEtats.append((joueur.nom, case, 0))

        # listeEtats = []
        # Distribution des graines sur le plateau
        while grainesEnMain:
            # Détection d'un retour sur case
            if changementDeCamp and camp is joueur and caseCourante == case:
                caseCourante += 1 if camp is self.joueur else -1

            # Distribution triviale
            if camp is self.joueur:
                if caseCourante <= self.nombreCasesJoueur - 1:
                    self.casesJoueur[caseCourante] += 1
                    self.listeEtats.append((self.joueur.nom, caseCourante, self.casesJoueur[caseCourante]))
                    derniereCase = caseCourante
                    caseCourante += 1

                elif caseCourante > self.nombreCasesJoueur - 1:
                    camp = self.CPU
                    caseCourante = self.nombreCasesJoueur - 1
                    grainesEnMain += 1
                    changementDeCamp = True

            elif camp is self.CPU:
                if caseCourante >= 0:
                    self.casesCPU[caseCourante] += 1
                    self.listeEtats.append((self.CPU.nom, caseCourante, self.casesCPU[caseCourante]))
                    derniereCase = caseCourante
                    caseCourante -= 1

                elif caseCourante < 0:
                    camp = self.joueur
                    caseCourante = 0
                    grainesEnMain += 1
                    changementDeCamp = True

            grainesEnMain -= 1

        # Manipulation de fin de tour
        if camp == adversaire:
            self.verifierPrises(derniereCase, joueur, adversaire)

        # VERIFICATION DES ETATS DU JEU
        self.verifierJeuSymetrique()
        self.verifierFinJeu(joueur, adversaire)
        self.verifierJeuNul()
        self.tourReussi = True

        self.precedent = precedent

    def retourSurPrecedent(self):
        return self.precedent

    def verifierJeuNul(self):
        self.estNul = True if self.joueur.grainesGagnees == self.CPU.grainesGagnees == 24\
                      else False
    
    def verifierJeuSymetrique(self):        
        self.compteurJeuSymetrique += 1

        if self.compteurJeuSymetrique == 30:
            self.estSymetrique = True
    
    def verifierPrises(self, derniereCase, joueur, adversaire):
        caseCourante = derniereCase

        if adversaire.cases[caseCourante] in [2, 3]:
             self.listeEtats.append("-")
        
        while adversaire.cases[caseCourante] in [2, 3]:
            self.compteurJeuSymetrique = 0

            self.listeEtats.append((adversaire.nom, caseCourante, 0))

            joueur.grainesGagnees += adversaire.cases[caseCourante]
            adversaire.cases[caseCourante] = 0

            caseCourante += -1 if adversaire is self.joueur else 1

            #Hors des limites du jeu
            if caseCourante in [-1, self.nombreCasesJoueur]:
                return
    
    def verifierFinJeu(self, joueur, adversaire):
        # L'adversaire est dans une impossibilité de jouer
        # Ceci regroupe <<bouffe-tout>> et <<cases d'un joueur vide et c'est à lui>>
        self.estFinal = True if self.casesVide(adversaire.cases) else False

        # Un joueur a plus de 24 graines gagnées
        self.estFinal += True if joueur.grainesGagnees > 24 else False
        self.estFinal += True if adversaire.grainesGagnees > 24 else False
        self.estFinal = bool ( self.estFinal )

        if self.estFinal:
            self.distribuerGrainesEnFace()
            if joueur.grainesGagnees > adversaire.grainesGagnees:
                self.gagnant = joueur
                self.perdant = adversaire
            else:
                self.gagnant = adversaire
                self.perdant = joueur

    def finCoupSurCase(self, case, joueur, adversaire):
        changementDeCamp = False
        camp = joueur
        caseCourante = case + 1 if joueur is self.joueur else case - 1
        derniereCase = caseCourante
        grainesEnMain = joueur.cases[case]

        # Simulation d'une distribution des graines sur le plateau
        while grainesEnMain:
            # Détection d'un retour sur case
            if changementDeCamp and camp is joueur and caseCourante == case:
                caseCourante += 1 if camp is self.joueur else -1

            # Distribution triviale
            if camp is self.joueur:
                if caseCourante <= self.nombreCasesJoueur - 1:
                    derniereCase = caseCourante
                    caseCourante += 1

                elif caseCourante > self.nombreCasesJoueur - 1:
                    camp = self.CPU
                    caseCourante = self.nombreCasesJoueur - 1
                    grainesEnMain += 1
                    changementDeCamp = True

            elif camp is self.CPU:
                if caseCourante >= 0:
                    derniereCase = caseCourante
                    caseCourante -= 1

                elif caseCourante < 0:
                    camp = self.joueur
                    caseCourante = 0
                    grainesEnMain += 1
                    changementDeCamp = True

            grainesEnMain -= 1

        return (camp, derniereCase)

    def distribuerGrainesEnFace(self):
        self.joueur.grainesGagnees += sum(self.joueur.cases)
        self.CPU.grainesGagnees += sum(self.CPU.cases)

    def tourJouable(self, case, joueur, adversaire):
        jouable = True

        if self.casesVide(adversaire.cases):
            if joueur == self.joueur:
                grainesSuffisantes = joueur.cases[case] >= 6-case
            else:
                grainesSuffisantes = joueur.cases[case] >= case + 1

            if not grainesSuffisantes:
                jouable = False

        print("jouable : ", jouable)

        return jouable

    def casesVide(self, cases):
        casesVides = [bool(i) for i in cases] == [0] * self.nombreCasesJoueur
        print("cases vides :", casesVides)
        return casesVides

    def grainesPresentes(self, case, joueur):
        return bool(joueur.cases[case])

    def afficherGain(self, nombreGraines, caseCourante, joueur, adversaire):
        values = (nombreGraines, self.parseOut(caseCourante), adversaire.nom, joueur.nom)
        print("GAIN : %d graine(s)\tSUR CASE : %d de %s\tBENEFICIAIRE : %s"%values)

    def etatJoueur(self):
        print("final : %s, nul : %s"%(self.estFinal, self.estNul))
        if self.estFinal:
            if self.gagnant is self.joueur:
                return 0
            elif self.perdant is self.joueur:
                return 2

        elif self.estNul:
            return 1

        else:
            return None

    def enregistrerStatistiquesJoueur(self):
        level = {2:0, 3:1, 5:2}[self.difficulte]
        etat = self.etatJoueur()

        if etat:
            print("statistiques.saveSession(self.joueur.nom, level, etat)")
        else:
            raise Exception("[ERREUR] Etat du jeu non enregistrable")

    def afficherAwale(self):
        print("  ".join([str(i) for i in range(1, self.nombreCasesJoueur + 1)]))
        print("-" * 16)
        A = [str(i) for i in self.casesCPU]
        B = [str(i) for i in self.casesJoueur]
        print("  ".join(A), self.CPU.nom, "\t Gain :", self.CPU.grainesGagnees)
        print("  ".join(B), self.joueur.nom, "\t Gain :", self.joueur.grainesGagnees)
        print("-" * 16)

    def parseIn(self, number):
        return number - 1

    def parseOut(self, number):
        return number + 1


if __name__ == "__main__":
    a = Awale("DDK")
    a.difficulte = 3
    j = lambda x : a.joueurJoue(x)
    c = lambda x : a.CPUJoue(x)
    af = lambda : a.afficherAwale()
    p = lambda : a.retourSurPrecedent()
