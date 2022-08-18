# ---------------------------------------------
# Executer les fonctions de la partie C
# ---------------------------------------------
from Partie_B import *
from Partie_C import *


def dernier_coup(coups, n_dernier):
    '''
    recevoir un dictionnaire coups et un numéro de dernier coup (la clé permettant
    d’accéder à la dernière configuration du plateau dans le dictionnaire), et qui renvoie le dernier coup joué, sous la
    forme d’une paire (tour de départ, tour d’arrivée)
    '''
    plateau = [coups[n_dernier]['Tour_1'], coups[n_dernier]
               ['Tour_2'], coups[n_dernier]['Tour_3']]
    n_avant = n_dernier-1
    plateau1 = [coups[n_avant]['Tour_1'], coups[n_avant]
                ['Tour_2'], coups[n_avant]['Tour_3']]
    i = 0
    while i <= 2:
        if (len(plateau[i]) < len(plateau1[i])):
            tour_depart = i
        elif (len(plateau[i]) > len(plateau1[i])):
            tour_arrivee = i
        i += 1

    return [tour_depart, tour_arrivee]


# Annuler dernier coup

def annuler_dernier_coup(coups, n_dernier):
    '''
    recevoir le dictionnaire coups et un numéro de dernier coup, et
    qui annule ce dernier coup. Il faut donc utiliser la fonction ci-dessus pour récupérer les coordonnées du dernier
    mouvement, et le jouer à l’envers. Mais il faut aussi penser à supprimer la dernière configuration du dictionnaire, et
    décrémenter le compteur de coups (égal à la plus grande clé de ce dictionnaire).
    '''
    ls = dernier_coup(coups, n_dernier)
    plateau = [coups[n_dernier]['Tour_1'], coups[n_dernier]
               ['Tour_2'], coups[n_dernier]['Tour_3']]
    a = plateau[ls[1]]
    n = len(plateau[0]) + len(plateau[1]) + len(plateau[2])
    nd = a[-1]
    efface_disque(nd, plateau, n)
    plateau[ls[0]].append(a[-1])
    plateau[ls[1]].remove(a[-1])
    b = plateau[ls[0]]
    nd = b[-1]
    dessine_disque(nd, plateau, n)
    del coups[n_dernier]['Tour_1']
    del coups[n_dernier]['Tour_2']
    del coups[n_dernier]['Tour_3']
    return coups
