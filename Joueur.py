
class Joueur:
    nomConfig = "joueur"
    def __init__(self, nom, cases):
        self.nom = nom
        self.grainesGagnees = 0
        self.cases = cases

    def __str__(self):
        return self.nom
