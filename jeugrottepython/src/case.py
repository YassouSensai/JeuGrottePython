class Case:
    def __init__(self, car):
        """
        Constructeur de la classe Case
        :param car: Une case sur un dur un fichier texte
        """
        self.terrain = car
        if str(self.terrain) == " " and str(self.terrain) not in ["#", "O"]:
            self.occupant = None
        if str(self.terrain) == ">" or str(self.terrain) == "<":
            self.occupant = self.terrain
        else:
            self.occupant = 0

    def __str__(self):
        """
        Affiche la case
        :return:    str(self.terrain)
        """
        return str(self.terrain)

    def libre(self):
        """
        Vérifie si la case est libre
        :return:    str(self.terrain) == " " (True si la case est libre, False sinon)
        """
        return str(self.terrain) == " "

    def depart(self):
        """
        Definit si la case est le départ ou non du terrain
        :return:    None
        """
        self.terrain = " "

    def arrivee(self, pion):
        """
        Définit si la case est l'arrivée ou non du terrain
        :param pion:
        :return:
        """
        if self.terrain == 'O':
            self.terrain = self.terrain
        else:
            self.terrain = pion