import time
import subprocess


for i in range(5, 0, -1):

    print("Lancement du projet")
    print(f"\nProjet JeuGrottePython : {__package__}")
    print(f"\nFichier  __init__.py : {__file__}")
    print(f"\nLancement de la partie dans :")
    print(i)
    time.sleep(1)
    subprocess.call("cls" if subprocess.os.name == "nt" else "clear", shell=True)