class Pion:
    def __init__(self, ligne, colonne, direction, jeu):
        """
        Constructeur de la classe Pion
        :param ligne:       L'indice de la ligne
        :param colonne:     L'indice de la colonne
        :param direction:   La direction du pion (1 ou -1)
        :param jeu:         Le jeu pour lequel le pion est créé
        :return:            None
        """
        self.l = ligne
        self.c = colonne
        self.d = direction
        self.jeu = jeu


    def __str__(self):
        """
        Affiche le pion selon la direction
        :return:    > si la direction est 1, < si la direction est -1
        """
        if self.d == 1:
            return '>'
        if self.d == -1:
            return '<'


    def avancer(self):
        """
        Permet de faire avancer le pion d'une case dans sa direction
        :return:    None
        """
        if self.d == 1:
            self.c += 1
        else:
            self.c -= 1

    def quitte(self):
        """
        Retire le pion du jeu
        :return:    None
        """
        self.jeu.pions.remove(self)

    def action(self):
        """
        Déplace ou retourne le pion
        :return:    None
        """
        if self.jeu.grotte[self.l+1][self.c].libre():   #Bloc pour les deplacements en bas dans le cas d'une case vide
            self.jeu.grotte[self.l][self.c].depart()
            self.l += 1
            self.jeu.grotte[self.l][self.c].arrivee(self)

        elif self.jeu.grotte[self.l+1][self.c].terrain == 'O':   #Bloc pour les deplacements en bas dans le cas d'une sortie
            self.jeu.grotte[self.l][self.c].depart()
            self.avancer()
            self.quitte()

        elif self.d == 1:   #Conditions si la direction du pion est de 1
            if self.jeu.grotte[self.l][self.c+1].libre():   #Bloc pour les deplacements a droite dans le cas d'une case vide
                self.jeu.grotte[self.l][self.c].depart()
                self.avancer()
                self.jeu.grotte[self.l][self.c].arrivee(self)

            if not self.jeu.grotte[self.l][self.c+1].libre():   #Bloc pour que le pion se retourne dans le cas d'une case non vide
                self.jeu.grotte[self.l][self.c].depart()
                self.d = -1
                self.jeu.grotte[self.l][self.c].arrivee(self)

            if  self.jeu.grotte[self.l][self.c+1].terrain == 'O':   #Bloc pour les deplacements a droite dans le cas d'une sortie
                self.jeu.grotte[self.l][self.c].depart()
                self.avancer()
                self.quitte()

        elif self.d == -1:   #Conditions si la direction du pion est de -1
            if self.jeu.grotte[self.l][self.c-1].libre():   #Bloc pour les deplacements a gauche dans le cas d'une case vide
                self.jeu.grotte[self.l][self.c].depart()
                self.avancer()
                self.jeu.grotte[self.l][self.c].arrivee(self)

            if not self.jeu.grotte[self.l][self.c-1].libre():   #Bloc pour que le pion se retourne dans le cas d'une case non vide
                self.d = 1
                self.jeu.grotte[self.l][self.c].depart()
                self.jeu.grotte[self.l][self.c].arrivee(self)

            if self.jeu.grotte[self.l][self.c-1].terrain == 'O':   #Bloc pour les deplacements a gauche dans le cas d'une sortie
                self.jeu.grotte[self.l][self.c].depart()
                self.avancer()
                self.quitte()
