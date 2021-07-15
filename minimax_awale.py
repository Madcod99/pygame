import awale
from copy import deepcopy as clone

class Minimax:
    def __init__(self,
                 awale : awale.Awale,
                 joueur,
                 adversaire,
                 caseMere):
        self.awale = awale
        self.joueur = joueur
        self.adversaire = adversaire
        self.profondeur = awale.difficulte
        self.caseMere = caseMere

    def indexMinimax(self):
        minimax1 = self.minimax()
        self.profondeur = 2
        minimax2 = self.minimax()

        print(minimax1, minimax2)

        try:minimax = [max(minimax1, minimax2)][-1]
        except: minimax = 0

        print(minimax, minimax2)

        return minimax[1] if type(minimax) is tuple\
               else minimax2
        
    def minimax(self):
        """
        Algorithme du minimax
        Entrées : noeud e, profondeur d
        Sorties : Valeur Minimax du noeud e

        SI final?(e) ou (d==0) ALORS
            RETURN h(e)

        SINON
            SI joueur?(e) ALORS
                RETURN max{ Minimax(e_i, d-1 | e_i € f(e)) }
            SINON
                RETURN min{ Minimax(e_i, d-1 | e_i € f(e)) }
        """
        
        # ETAT FINAL
        if self.estFinal() or self.profondeur == 0:
            return self.heuristique()

        # ETAT NON FINAL
        else:
            # GENERATION DES FILS DE L'ETAT COURANT
            filsEtat = self.filsEtat()
            valeursMinimaxFils = []

            # EVALUATION DES FILS DE L'ETAT COURANT
            for case in range(self.awale.nombreCasesJoueur):
                fils = filsEtat[case]
                if fils : fils.difficulte -= 1
                if fils is not None:
                    minimax = Minimax(fils,
                                      self.adversaire,
                                      self.joueur,
                                      case
                                      ).minimax()

                    signe = -1 if self.joueur == self.awale.joueur else 1

                    if type(minimax) is int:
                        valeursMinimaxFils.append(minimax)

                    elif type(minimax) is tuple:
                        valeursMinimaxFils.append(minimax[0])

                    else:
                        valeursMinimaxFils.append( self.alphaBeta(self.heuristique()) )

                elif fils is None:
                    # LE FILS N'EST PAS JOUABLE
                    valeursMinimaxFils.append(None)       

            # ON MAXIMISE LE GAIN DU CPU EN MINIMISANT CELUI DU JOUEUR
            return self.valeurMinimax(valeursMinimaxFils)

    def valeurMinimax(self, valeurs):
        """Valeur du Minimax d'un noeud parmi les valeurs minimax des fils"""
        valeursEvaluables = [i for i in valeurs if i is not None]
        VAL = max(valeursEvaluables) if valeursEvaluables else 0
        
        plusieursPossibilites = True if valeurs.count(VAL) > 1 else False

        if plusieursPossibilites:
            indexListe = []
            for i in range(len(valeurs)):
                if valeurs[i] == VAL:
                    indexListe.append(i)

            INDEX = self.choisirCaseJouable(indexListe)
        else :
            try :
                INDEX = valeurs.index(VAL) if valeursEvaluables is not None\
                        else self.choisirCaseJouable(list(range(1, 7)))
            except :
                INDEX = self.choisirCaseJouable(list(range(1, 7)))

        return (VAL, INDEX)

    def alphaBeta(self,valeur):
        return None if (valeur < -12 or valeur > 22) and (valeur not in [1000, -1000]) else valeur
        
    def heuristique(self):
        """Heuristique d'évaluation d'un état"""
        if self.estFinal():
            if self.estGagnant():
                return 1000
            else:
                return -1000

        else:
            difference = self.awale.CPU.grainesGagnees \
                         - self.awale.joueur.grainesGagnees

            vulnerabilite = self.evaluerVulnerabilite()
            
            evaluation = difference

            return evaluation * (1 - vulnerabilite)

    def evaluerVulnerabilite(self):
        _1 = self.awale.CPU.cases.count(1) / self.awale.nombreCasesJoueur
        _2 = self.awale.CPU.cases.count(2) / self.awale.nombreCasesJoueur

        vulnerabilite = (_1*0.4 + _2*0.6) if _1 or _2 else 0
        

        return vulnerabilite

    def filsEtat(self):
        """Génération des fils d'un état"""
        fils = {}

        for case in range(self.awale.nombreCasesJoueur):
            etatFils = clone(self.awale) \
                       if self.joueur.cases[case] \
                       else None

            if etatFils:            
                if self.joueur.nom == "CPU":
                    etatFils.CPUJoue(case+1)
                else:
                    etatFils.joueurJoue(case+1)
            
            fils[case] = etatFils            

        return fils

    def estFinal(self):
        return self.awale.joueur.grainesGagnees >= 24 \
               or self.awale.CPU.grainesGagnees >= 24

    def estGagnant(self):
        return (self.awale.CPU.grainesGagnees\
                - self.awale.joueur.grainesGagnees) > 0

    def choisirCaseJouable(self, cases):

        for case in cases:
            tourJouable = self.awale.tourJouable(case, self.joueur, self.adversaire)
            grainesPresentes = self.awale.grainesPresentes(case, self.joueur)

            if tourJouable and grainesPresentes:
                return case

def test():
    v = r()
    print()
    af()
    v_ = a.parseOut(v)
    print( "JOUER : %i => %i"%(v, v_) )
    c( v_ )
    af()
def simulation():
    while 1:
        j( int(input("Votre case : ")) )
        af()
        test()
    
if __name__ == "__main__":
    profondeurMAX = 4
    a = awale.Awale("DDK")
    m = Minimax(a, a.CPU, a.joueur, None)
    j = lambda x : m.awale.joueurJoue(x)
    c = lambda x : m.awale.CPUJoue(x)
    r = lambda : m.indexMinimax()
    af = lambda : m.awale.afficherAwale()
