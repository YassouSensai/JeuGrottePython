import os
import random
from jeu import Jeu

repertoireCircuits = "circuits"
listeCircuits = [circuit for circuit in os.listdir(repertoireCircuits) if circuit.endswith(".txt")]


if __name__ == "__main__":
    circuit = random.choice(listeCircuits)
    j = Jeu("circuits/" + circuit)
    j.demarre()