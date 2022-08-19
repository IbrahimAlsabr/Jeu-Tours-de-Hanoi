# Jeu Les tours de Hanoi

Il s'agit d'un projet Les tours de Hanoi de l'UE INF101 pour le parcours Informatiqe de première année à l'université Grenoble Alpes.

## Tableau De Contenu

-   [Introduction](#introduction)

    -   [Règles](#Règles)
    -   [Structures de données](#structures-de-données)

-   [Installation de l'environnement](#installation-de-l'environnement)

    -   [Windows](#windows)
    -   [Linux](#linux)

-   [Préparation du projet](#préparation-du-projet)
-   [Utilisation](#utilisation)

-   [Mon Travail](#mon-travail)
    -   [Autour Fichiers](#autour-fichiers)
    -   [Créer avec](#créer-avec)
    -   [Resources et outils utiles](#resources-et-outils-utiles)
-   [Author](#author)
-   [Acknowledgments](#acknowledgments)

## Introduction

### Règles

Les tours de Hanoi sont un jeu de réflexion consistant à déplacer des disques de différents diamètres, d’une tour de départ à une tour d’arrivée, en passant par une tour intermédiaire, en un minimum de coups, tout en respectant les règles suivantes:

-   on ne peut déplacer qu’un seul disque à la fois
-   on ne peut pas placer un disque sur un disque plus petit que lui

Dans la configuration de départ, les disques sont empilés en ordre décroissant de taille sur la tour de gauche. Dans la
configuration finale, ils doivent etre empilés dans le mˆeme ordre décroissant, mais sur la tour de droite. Dans le problème
classique, il y a 3 disques, et il suffit de 7 coups pour les déplacer d’une tour à l’autre. Dans le problème général à n
disques, il faut 2<sup>n</sup> − 1 coups au minimum pour déplacer tous les disques. <br>

![jeu](doc/jeu.jpg?raw=true")

### Structures de données

<p>
On note n le nombre de disques. On représente ces disques par des numéros : le plus petit disque porte le numéro 1, le
plus grand disque porte le numéro n.
On représente le plateau de jeu par une liste plateau. Celle-ci contient 3 listes, une par tour (départ à l’indice 0,
auxiliaire à l’indice 1, arrivée à l’indice 2). Dans chaque liste représentant une tour, le numéro du disque le plus bas est
à l’indice 0, et le dernier élément est le numéro du disque le plus haut. S’il n’y a aucun disque sur une tour, la liste
correspondante est vide.
Par exemple, sur l’image ci-dessus, la configuration de départ est représentée par la liste plateau suivante: [ [ 3, 2, 1 ], [ ], [ ] ].
La tour de départ (indice 0) contient donc tous les disques, le plus gros en bas, puis le moyen, puis le petit en haut; la
tour auxiliaire et la tour d’arrivée ne contiennent aucun disque (listes vides). Si on déplace le petit disque sur la tour
auxiliaire, on obtient la liste plateau suivante: [ [3 , 2 ], [1], [ ] ]. La tour de départ ne contient plus que les disques numéro 3
(le plus grand) et 2 (le moyen); la tour auxiliaire contient le petit disque (numéro 1); la tour d’arrivée ne contient aucun
disque. La configuration d’arrivée est [ [ ], [ ], [ 3, 2, 1 ] ] (tous les disques sur la tour de droite).
</p>

## Installation de l'environnement

### Windows

Installer Python 3 avec l'installeur disponible sur le site officiel:

-   64 bits (à préférer): https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe
-   32 bits (au cas où): https://www.python.org/ftp/python/3.9.2/python-3.9.2.exe

Suivre les étapes de l'installeur. S'assurer que l'option "Ajouter à la
variable d'environnement PATH" est bien cochée.

### Linux

#### Debian/Ubuntu

Dans un terminal:

    sudo apt install -y python3

## Préparation du projet

Une fois Python installé, il faut installer la bibliothèque Turtle. Dans un terminal :

    python3 -m pip install --user PythonTurtle
    PythonTurtle

## Utilisation

Dans un terminal :

    python3 main.py

Cela va exécuter la méthode main contenue dans le script `main.py`.

## Mon Travail

### Autour Fichiers

<b>Partie A :</b> <b style="color: #15adc0">Plateau de jeu et listes</b>
Dans cette partie, on a commencé par la fonction <b> init(n)</b> qui permet de renvoyer la configuration initiale de plateau. A partir de nombre de disques reçu en paramètre, cette fonction crée une liste des entiers classés par ordre décroissant pour la tour de gauche (indice 0 de la liste plateau).
La deuxième fonction <b>nombre_disque(plateau, numtour)</b> affiche le nombre de disques qui se trouvent dans la tour renseignée. Le principe c’est de mesurer la taille de la liste correspondante à la tour en utilisant la fonction len().
Ensuite, les fonctions <b>disque_superieur(plateau, numtour)</b> et <b>position_disque(plateau, numdisque)</b> permettent de récupérer le numéro du disque supérieur de la tour (en affichant le dernier élément de la lise (plateau[numtour][-1])) pour la première et le numéro de la tour où se positionne le disque pour la deuxième.
Dans la fonction <b>verifier_deplacement(plateau, nt1, nt2)</b>, on a utilisé la fonction <b> disque_superieur(plateau, numtour)</b>pour vérifier si le déplacement qui a demandé l’utilisateur est possible ou pas, en utilisant la fonction disque_superieur définie avant.

```python
def verifier_deplacement(plateau,nt1,nt2):
  if plateau[nt1]!=[] and plateau[nt2]==[]:
    return True
  elif plateau[nt1]!=[] and plateau[nt2]!=[]:
    if disque_superieur(plateau,nt2) > disque_superieur(plateau,nt1):
      return True
    else:
      return False
```

La dernière fonction vérifie si les disques sont tous bien positionnés dans la troisième tour, ce qui correspond à la situation de la victoire des tours de Hanoi.

<b >Partie B :</b> <b style="color: #15adc0">Graphisme avec Turtle</b>
Cette partie concerne le graphisme avec Turtle. La première fonction dessine le plateau en fonction de nombre de disques renseignés par l’utilisateur. On a commencé par introduire les mesures de la figure pour le cas d’un seul disque. Ces mesures augmentent en lien avec le nombre n de disques.
La fonction <b>dessine_disque(nd, plateau, n)</b>
permet de dessiner le disque en se basant sur sa position sur le plateau, donnée par la configuration de ce dernier. <b>efface_disque(nd, plateau, n)</b> est basée sur le même principe en dessinant cette fois en blanc par-dessus.
La fonction <b>dessine_config(plateau, n)</b> fait appel à la fonction <b>dessine_disque()</b> pour dessiner chaque disque de plateau afin d’avoir la configuration finale de plateau.

<b>Partie C :</b> <b style="color: #15adc0">Interactions avec le joueur</b>
Cette partie consiste à interagir avec le joueur. Elle commence par la fonction <b>lire_coords(plateau)</b> qui permet au joueur d’entrer le déplacement qu’il souhaite effectuer sur le plateau et vérifier au même temps s’il est possible. Dans le cas contraire, il redemande à l’utilisateur d’entrer des coordonnées valides.
La fonction <b>jouer_un_coup(plateau, n)</b> effectue ce déplacement, en utilisant les fonction dessine et efface disque définies dans la partie B, en plus de la fonction disque_configuration pour tracer le plateau et les autres disques
La fonction <b>boucle_jeu(plateau, n)</b> regroupe les deux premières fonction pour permettre à l’utilisateur de jouer jusqu’à ce qu’il gagne, en vérifiant à chaque fois s’il atteint la configuration finale avec la fonction verifier_victoire(). On a également fixé un nombre maximal de coups à jouer, et on a donné à l’utilisateur le droit de quitter la partie en saisissant la valeur -1 comme tour de départ.
En fin, dans le programme principale on demande au joueur d’entrer le nombre de disques, pour lancer après la boucle de jeu avec la fonction boucle jeu.

<b>Partie D :</b> <b style="color: #15adc0"> Annulation de coups</b>
L’objectif de cette partie c’est de permettre au joueur d’annuler son dernier coup et de revenir en arrière. Pour cela on a utilisé un dictionnaire qui enregistre à chaque fois la configuration du plateau après chaque coup.
Le problème qu’on a rencontré dans cette partie c’est par rapport à l’ajout des éléments dans le dictionnaire. En fait, quand on rajoute une nouvelle valeur on perd les anciennes parce qu’ils se remplacent toutes par la nouvelle valeur.
Après chaque coup, on demande au joueur s’il voulait annuler son dernier coup. Pour cela, on a modifié la fonction boucle_jeu pour qu’il autorise l’annulation du dernier coup.

```python
def annuler_dernier_coup(coups , n_dernier) :
    ls = dernier_coup(coups , n_dernier)
    plateau = [coups[n_dernier]['Tour_1'], coups[n_dernier]['Tour_2'], coups[n_dernier]['Tour_3']]
    a=plateau[ls[1]]
    n = len(plateau[0]) + len(plateau[1]) + len(plateau[2])
    nd = a[-1]
    efface_disque(nd,plateau,n)
    plateau[ls[0]].append(a[-1])
    plateau[ls[1]].remove(a[-1])
    b = plateau[ls[0]]
    nd = b[-1]
    dessine_disque(nd,plateau,n)
    del coups[n_dernier]['Tour_1']
    del coups[n_dernier]['Tour_2']
    del coups[n_dernier]['Tour_3']
    return coups
```

<b>Partie E : </b> <b style="color: #15adc0"> Fichier de scores et temps de jeu</b>
L’objectif de cette partie est d’enregistrer les scores des joueurs dans un fichier, pour pouvoir les comparer par la suite.
Tout d’abord on a commencé par écrire une fonction qui enregistre le score du joueur en tenant compte de 3 informations dans un fichier de scores :

-   Nom du joueur
-   Nombre de disques
-   Nombre de coups
    On a choisi de sauvegarder ces données dans un fichier binaire de type Pickle. Donc, au niveau du programme principal <b>Programme.py</b>, on a importé le module Pickle :

```python
import pickle
```

A la fin de la partie du joueur, on met à jour le dictionnaire des scores par les informations du joueur.

```python
nom = str(input("Ecrire votre nom :"))
    dictionnaire_score[nom] = {}
    dictionnaire_score[nom]["nb_disque"] = n
    dictionnaire_score[nom]["nb_coups"] = donnees[0]
    dictionnaire_score[nom]["time"] = time.time() - start_time
```

On crée le fichier binaire et on appelle la méthode dump pour écrire dans le fichier Scores_Des_Joueurs.pickle les informations du joueur

```python
# creation du fichier Pickle
        pickle_out = open("Scores_Des_Joueurs.pickle","wb")
        pickle.dump(dictionnaire_score, pickle_out)
        pickle_out.close()
```

Une fois qu’on a recueilli les informations de tous les joueurs, on lit le fichier binaire de type Pickle et on appelle la fonction afficher_meilleurs_scores.

```python
#Lecture du fichier
pickle_in = open("Scores_Des_Joueurs.pickle","rb")
example_dictio = pickle.load(pickle_in)
# Meilleurs scores (nombre de coups)
afficher_meilleurs_scores(example_dictio)
```

Voici l’implémentation de cette fonction.

```python
def afficher_meilleurs_scores(dict_des_resultats) :
    #print (dict_des_resultats)
    dic_meilleurs_scores = {}
    for key, value in dict_des_resultats.items():
        for cles,valeurs in value.items():
            if(cles == "nb_coups") :
                dic_meilleurs_scores[key] = valeurs
    print(sorted(dic_meilleurs_scores.items(), key = lambda kv:(kv[1], kv[0])))
    return
```

On crée un dictionnaire des meilleurs scores contenant les noms des participants (Clé) et leurs nombre de coups respectifs (Valeur) et on utilise la méthode sorted pour trier ce dictionnaire dans l’ordre croissant.

<b >Partie F :</b> <b style="color: #15adc0">Jeu automatique, fonction récursive</b>
L’objectif de cette est de créer une fonction capable de trouver la liste optimale des mouvements à jouer pour déplacer n disques de la tour de départ à la tour d’arrivée.
On a créé une fonction récursive Tour Hanoi ayant comme paramètres le nombre de disques, la tour de départ, la tour d’arrivée et la tour auxiliaire.

```python
def Tour_Hanoi(n , tour_depart, tour_arrive, tour_auxiliare):
    if n == 1:
        print ("Deplacer le disque 1 de la tour",tour_depart,"a la tour",tour_arrive)
    return
    Tour_Hanoi(n-1, tour_depart, tour_auxiliare, tour_arrive)
    print ("Deplacer le disque",n,"de la tour",tour_depart,"a la tour",tour_arrive )
    Tour_Hanoi(n-1, tour_auxiliare, tour_arrive, tour_depart)
```

### Créer avec

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### Resources et outils utiles

-   [Python Documentation](https://docs.python.org/fr/3/)
-   [Geeks for Geeks](https://www.geeksforgeeks.org/)

## Author

<b> Ibrahim Alsabr </b>

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IbrahimAlsabr) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ibrahim-alsabr-188939231/) [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/home?lang=fr) <br>

## Acknowledgments

-   [Université Grenoble Alpes](https://www.univ-grenoble-alpes.fr/)
