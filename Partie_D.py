#---------------------------------------------
# Executer les fonctions de la partie C
#---------------------------------------------

exec(open('C:/Users/ibrah/Documents/Presentation_Python/Partie_C.py').read())
exec(open('C:/Users/ibrah/Documents/Presentation_Python/Partie_B.py').read())



def dernier_coup(coups , n_dernier) :
    plateau = [coups[n_dernier]['Tour_1'], coups[n_dernier]['Tour_2'], coups[n_dernier]['Tour_3']]
    n_avant = n_dernier-1
    plateau1 = [coups[n_avant]['Tour_1'], coups[n_avant]['Tour_2'], coups[n_avant]['Tour_3']]
    i = 0
    while i<=2 :
        if(len(plateau[i]) < len(plateau1[i])):
            tour_depart = i
        elif (len(plateau[i]) > len(plateau1[i])):
            tour_arrivee = i
        i+=1
        
    return [tour_depart, tour_arrivee]


# Annuler dernier coup

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

