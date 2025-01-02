from jeugrottepython.src.case import Case
from jeugrottepython.src.pion import Pion

class Jeu:
    def __init__(self, nom_de_carte):
        """
        Constructeur de la classe Jeu
        :param nom_de_carte: le nom du fichier contenant la carte
        :return:    None
        """
        carte = open(nom_de_carte)
        self.grotte = [[Case(car) for car in ligne if car != '\\n'] for ligne in carte.readlines()]
        self.pions = []

    def affiche(self):
        """
        Affiche la grotte
        :return:    None
        """
        for ligne in self.grotte:
            for case in ligne:
                print(case, end="")

    def raffraichir_ecran(self):
        """
        Permet "d'effacer", de rajouter des espaces entre chaques affichages dans un objectif "encadrement"
        :return:    None
        """
        nb = len(self.grotte)
        clear = "\n"  * nb
        print(clear)


    def entree(self):
        """
        Permet de savoir sur quelle colonne se trouve l'entrée
        :return:    c: la colonne
        """
        c = 0       # la colonne
        n = " "     # le caractère qui definit l'entrée sur la première ligne
        d = ""      # création d'une chaîne de caractère qui permettra de trouver la position de "n"
        for ligne in self.grotte:
            for i in range(len(self.grotte[0])):
                d += str(self.grotte[0][i])
                c = d.find(n)
        return c

    def tour(self):
        """
        Fait agir chaque pion une fois et affiche le nouvel état du jeu
        :return:    None
        """
        self.raffraichir_ecran()
        for PIONS in self.pions:
            PIONS.action()
        self.affiche()

    def demarre(self):
        """
        Lance une boucle infinie et reçoit les commandes
        :return:    None
        """
        self.affiche()
        play = 1
        while play == 1:
            demarrons_le_jeu = input("\nQue voulez-vous faire ?\nVoici les règles du jeu:\n - Entrez un '+' pour ajouter un pion\n -Appuyez sur la touche 'entrée' pour jouer un tour\n - Entrez un 'q' pour quitter la partie\n")

            if demarrons_le_jeu == '+':
                self.raffraichir_ecran()
                a = (Pion(0, self.entree(), 1, self))                    #definit un pion "a" au niveau de l'entrée
                if self.grotte[a.l][self.entree()].libre():              #test si l'entrée est libre afin d'inserer le pion "a" en jeu ou non
                    self.pions.append(a)
                else:
                    pass

                for PIONS in self.pions:
                    self.grotte[PIONS.l][PIONS.c] = Case(PIONS)         #place les pions à leur position dans le jeu
                self.affiche()

            if demarrons_le_jeu == '':
                self.tour()                                             #applique la fonction tour() si on appuie sur la touche Entrée

            if demarrons_le_jeu == 'q':
                print("Vous avez quitté le jeu !")
                play = 0

            if demarrons_le_jeu != '+' and demarrons_le_jeu != '' and demarrons_le_jeu != 'r' and demarrons_le_jeu != 'q':
                print("\nNous ne comprenons pas ce que vous voulez faire !")