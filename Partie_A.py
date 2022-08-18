def init(n):
    """
    Cette fonction pour recevoir en argument un entier n (le nombre de disques), et qui renvoie la liste
    représentant la configuration initiale du plateau, c’est-a-dire avec les n disques (numérotés de 1 à n) empiles dans
    l’ordre d´écroissant de taille (et donc aussi de numéro), sur la tour de gauche (`a l’indice 0 de la liste plateau); les
    autres tours (milieu et droite) sont vides.
    """
    plateau = [[], [], []]
    i = 0
    while i < n:
        j = 1
        while n >= j:
            plateau[0].insert(i, n)
            n -= 1
            i += 1
    return plateau
    # print(init(5))


def nombre_disque(plateau, numtour):
    """ Cette fonction pour recevoir la configuration courante du plateau et un
        numéro de tour (entre 0 et 2, supposé correct), et qui renvoie le nombre de disques sur cette tour.
    """
    if numtour > 2 or numtour < 0:
        a = "supposé incorrect"
    else:
        a = len(plateau[numtour])
    return a


def disque_superieur(plateau, numtour):
    """
    Cette fonction pour recevoir la configuration courante du plateau et un
    numéro de tour (entre 0 et 2, supposé correct), et qui renvoie le numéro du disque supérieur de cette tour (ou -1 si
    la tour est vide).
    """
    if numtour > 2 or numtour < 0:
        max = "supoosé incorrect"
    else:
        a = list(plateau[numtour])
        if a == []:
            max = -1
        else:
            max = a[0]
    return max
# print(disque_superieur([[5,4],[3,2,1],[]],1))


def position_disque(plateau, numdisque):
    """
    Cette fonction pour recevoir la configuration courante du plateau et un
    numéro de disque (entre 1 et n, supposé correct), et qui renvoie sa position, c’est-`a-dire le numéro de la tour (entre
    0 et 2) sur laquelle il est placé. Remarque: le disque est forcément présent puisque le numéro reçu est correct
    """
    i = 0
    while i < len(plateau):
        if numdisque in plateau[i]:
            position = i
        i += 1
    return position
# print(position_disque([[5,4],[3,2],[1]],4))


def verifier_deplacement(plateau, nt1, nt2):
    """ 
    Cette fonction pour recevoir en argument une configuration du
    plateau, une position initiale et une position finale, et qui renvoie un booléen indiquant si ce déplacement est
    autorisé. Rappel: pour qu’un déplacement soit autorisé il faut qu’il y ait un disque dans la tour nt1, et que la
    tour nt2 soit vide ou contienne un disque plus grand que celui qu’on veut y poser. Il faut donc utiliser la fonction
    disque superieur sur ces tours
    """
    if plateau[nt1] != [] and plateau[nt2] == []:
        return True

    elif plateau[nt1] != [] and plateau[nt2] != []:
        if disque_superieur(plateau, nt2) > disque_superieur(plateau, nt1):
            return True
        else:
            return False
# print(verifier_deplacement([[6,5,4],[3],[2,1]],1,2))


def verifier_victoire(plateau, n):
    """
    Cette fonction pour recevoir en argument la configuration du plateau et le
    nombre de disques, et qui vérifie si on a atteint la solution, c’est-`a-dire les n disques empilés dans l’ordre décroissant
    de taille (de n `a 1) sur la tour de droite (la derni`ere de la liste plateau).
    """
    i = 0
    plateau1 = [[], [], []]
    while i < n:
        j = 1
        while n >= j:
            plateau1[2].insert(i, n)
            n -= 1
            i += 1
        if plateau1 == plateau:
            a = True
        else:
            a = False
    return a
# print(verifier_victoire([[],[],[6,5,4,3,2,1]],6))
