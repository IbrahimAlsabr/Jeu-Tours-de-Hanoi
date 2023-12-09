# Jeu des Tours de Hanoï

Ce projet a été réalisé dans le cadre de l'UE INF101 du parcours Informatique de première année à l'Université Grenoble Alpes.

## Tableau de Contenu

- [Introduction](#introduction)
  - [Règles du Jeu](#règles-du-jeu)
  - [Structures de Données](#structures-de-données)
- [Installation de l'Environnement](#installation-de-lenvironnement)
  - [Windows](#windows)
  - [Linux](#linux)
- [Préparation du Projet](#préparation-du-projet)
- [Utilisation](#utilisation)
- [Créé avec](#créé-avec)
- [Ressources et Outils Utiles](#ressources-et-outils-utiles)
- [Auteur](#auteur)

## Introduction

### Règles du Jeu

Le jeu des Tours de Hanoï est un jeu de réflexion consistant à déplacer des disques de différents diamètres d'une tour de départ à une tour d'arrivée, en passant par une tour intermédiaire, en un minimum de coups, tout en respectant les règles suivantes :

- On ne peut déplacer qu'un seul disque à la fois.
- On ne peut pas placer un disque sur un disque plus petit que lui.

Dans la configuration de départ, les disques sont empilés en ordre décroissant de taille sur la tour de gauche. Dans la configuration finale, ils doivent être empilés dans le même ordre décroissant, mais sur la tour de droite. Dans le problème classique, il y a 3 disques, et il suffit de 7 coups pour les déplacer d'une tour à l'autre. Dans le problème général avec n disques, il faut 2<sup>n</sup> − 1 coups au minimum pour déplacer tous les disques.

![jeu](doc/jeu.jpg?raw=true)

### Structures de Données

On note n le nombre de disques. Chaque disque est représenté par un numéro, le plus petit disque porte le numéro 1, et le plus grand porte le numéro n. Le plateau de jeu est représenté par une liste appelée "plateau". Cette liste contient trois sous-listes, une pour chaque tour (départ à l'indice 0, auxiliaire à l'indice 1, arrivée à l'indice 2). Dans chaque sous-liste représentant une tour, le numéro du disque le plus bas est à l'indice 0, et le dernier élément est le numéro du disque le plus haut. Si une tour est vide, la sous-liste correspondante est vide.

Par exemple, la configuration de départ est représentée par la liste plateau suivante : `[ [ 3, 2, 1 ], [ ], [ ] ]`. La tour de départ (indice 0) contient tous les disques, le plus gros en bas, puis le moyen, puis le petit en haut. La tour auxiliaire et la tour d'arrivée ne contiennent aucun disque. Si on déplace le petit disque sur la tour auxiliaire, on obtient la liste plateau suivante : `[ [3 , 2 ], [1], [ ] ]`. La tour de départ ne contient plus que les disques numéro 3 (le plus grand) et 2 (le moyen), la tour auxiliaire contient le petit disque (numéro 1), et la tour d'arrivée ne contient aucun disque. La configuration d'arrivée est `[ [ ], [ ], [ 3, 2, 1 ] ]` avec tous les disques sur la tour de droite.

## Installation de l'Environnement

### Windows

Pour installer Python 3 sur Windows, téléchargez l'installeur disponible sur le [site officiel de Python](https://www.python.org/downloads/windows/). Vous pouvez choisir entre la version 64 bits et 32 bits, mais la version 64 bits est recommandée. Suivez les étapes de l'installeur en vous assurant de cocher l'option "Ajouter à la variable d'environnement PATH".

### Linux

#### Debian/Ubuntu

Pour installer Python 3 sur Debian/Ubuntu, ouvrez un terminal et exécutez la commande suivante :

    sudo apt install -y python3

## Préparation du Projet

Une fois Python installé, vous devez installer la bibliothèque Turtle en utilisant pip. Ouvrez un terminal et exécutez les commandes suivantes :

    python3 -m pip install --user PythonTurtle
    PythonTurtle

## Utilisation

Pour lancer le jeu, ouvrez un terminal et exécutez la commande suivante :

    python3 main.py

Cela exécutera la méthode `main` contenue dans le script `main.py`.

### Créer avec

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## Author

<b> Ibrahim Alsabr </b>

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IbrahimAlsabr) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ibrahim-alsabr-188939231/) [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/home?lang=fr) <br>
