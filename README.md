# JeuGrottePython

## Auteur : ELKHALKI Yassine

![exemple_jeu.png](images%2Fexemple_jeu.png)

## Sommaire
1. [Introduction](#Introduction)
2. [Description](#Description)
3. [Fonctionnement](#Fonctionnement)


# Introduction

Ce projet est un jeu de la grotte en python. Il a été réalisé dans le cadre de la spécialité NSI en début d'année de terminale.
Il s'agit d'un jeu qui avait pour objectif d'avoir un premier contact avec les bases de la programmation objet en python.  
  

Le jeu implémenté ici vient ajouter un ou plusieurs pion(s) ('>' ou '<') dans un circuit de grotte. Le joueur a uniquement la possibilité
de le faire avancer ou reculer en fonction de la configuration du circuit afin d'amener les pions à la sortie de la grotte.  
  
Il s'agit d'un jeu très simple, mais qui nécessite tout de même de la réflexion pour des débutants en programmation.


# Description
Ce projet est composé de plusieurs fichiers dont plusieurs classes qui permettent de gérer le jeu. Il y a donc les fichiers suivants : 
* **case.py :** Ce fichier contient la classe Case qui permet de gérer les cases du circuit de la grotte.
* **pion.py :** Ce fichier contient la classe Pion qui permet de gérer les pions qui se déplacent dans la grotte.
* **jeu.py :** Ce fichier contient la classe Jeu qui permet de gérer le jeu de la grotte.
* **lancer_partie.py :** Ce fichier permet de lancer une partie de la grotte.

Il y a également un dossier **circuit** qui contient les différents circuits de la grotte.


# Fonctionnement
Pour lancer une partie du jeu, il suffit d'éxecuter le projet avec la commande suivante à la racine du projet : 

```shell
python -m jeugrottepython
```

En effet, la commande précédente executera le fichier [__main__.py](./jeugrottepython/__main__.py) qui contient déjà les instructions nécessaires au lancement d'une partie (voir ci-dessous)

```python
if __name__ == "__main__":
    circuit = random.choice(listeCircuits)
    j = Jeu(os.path.join(repertoireCircuits, circuit))
    j.demarre()
```  
  

Une fois lancé, les instructions suivantes vous seront données dans la console python : 
```txt
###### ########
#             #
##### #########
#         #   #
#  ########   #
#             #
########  #####
       #  #
       #O##  

Que voulez-vous faire ?
Voici les règles du jeu:
 - Entrez un '+' pour ajouter un pion
 - Appuyez sur la touche 'entrée' pour jouer un tour
 - Entrez un 'q' pour quitter la partie
```