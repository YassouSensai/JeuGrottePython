import os
import random
from jeugrottepython.src import Jeu

repertoireCircuits = os.path.join(os.getcwd(), "jeugrottepython", "src", "circuits")
print(os.getcwd())

listeCircuits = [circuit for circuit in os.listdir(repertoireCircuits) if circuit.endswith(".txt")]


if __name__ == "__main__":
    circuit = random.choice(listeCircuits)
    j = Jeu(os.path.join(repertoireCircuits, circuit))
    j.demarre()