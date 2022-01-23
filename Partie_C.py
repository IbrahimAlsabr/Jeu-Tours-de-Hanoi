import collections
from copy import deepcopy


def merge(dict1, dict2):
    ''' Return a new dictionary by merging two dictionaries recursively. '''

    result = deepcopy(dict1)

    for key, value in dict2.items():
        if isinstance(value, collections.Mapping):
            result[key] = merge(result.get(key, {}), value)
        else:
            result[key] = deepcopy(dict2[key])

    return result
#---------------------------------------------
# Executer les fonctions de la partie B
#---------------------------------------------

exec(open('C:/Users/ibrah/Documents/Presentation_Python/Partie_B.py').read())


#---------------------------------------------
# Les fonctions de la partie C
#---------------------------------------------

def lire_coords(plateau) :
    
  valid = False
  probleme = False
  n_arrivee = -1
  while not(valid) or probleme :
    n_depart = int(input("Entrer le numéro du départ :"))
    if(n_depart == -1) :
          verif = str(input("Vous souhaitez abandonner le jeu ? (o/n)"))
          if(verif == "o") :
                break      
          else:
                probleme = True
    elif(n_depart >= 0 and n_depart <= 2) :
          if(plateau[n_depart] == []) :
              print("Invalide, tour vide")
              probleme = True
          else : 
              n_arrivee =  int(input("Entrer le numéro d'arrivée :"))
              if(n_arrivee >= 0 and n_arrivee <=2):
                    if(plateau[n_arrivee] == [] or plateau[n_arrivee][-1] > plateau[n_depart][-1]) :
                          valid = True
                          probleme = False
                    elif(plateau[n_arrivee][-1] < plateau[n_depart][-1]) :
                          print("Invalide, disque plus petit")
                          probleme = True
              else :
                    print("Invalide")
                    probleme = True
    else :
          print("Invalide")
          probleme = True        

  return [n_depart, n_arrivee]    




def jouer_un_coup(plateau,n):  
  dissque_config(plateau,n)
  ls= lire_coords(plateau) 
  if(ls[0]!=ls[1]) :
        a=plateau[ls[0]]
        nd = a[-1]
        efface_disque(nd,plateau,n)
        plateau[ls[1]].append(a[-1])
        plateau[ls[0]].remove(a[-1])
        b = plateau[ls[1]]
        nd = b[-1]
        dessine_disque(nd,plateau,n)

  else:
         print("Vous avez quitté le jeu")
         plateau = [[],[],[]]
  
  return plateau
  

#print(jouer_un_coup([[3,2],[],[1]],3))
#print(dessine_plateau(3))


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
    del coups[n_dernier]
    return coups


#coups = {1 : [[3,2],[1],[]], 2 : [[3],[1],[2]]}

#print(dernier_coup(coups, 2))
#print(annuler_dernier_coup(coups, 2))


  
def boucle_jeu(plateau, n):
  n_coups = 1
  max=100
  victoire = False
  coups = {0 : {'Tour_1' : plateau[0],
                 'Tour_2' : plateau[1],
                 'Tour_3' : plateau[2]}}
  plat = plateau
  print(coups)
  while not(victoire) and n_coups < max :
        print("Coup numéro", n_coups)
        #coups.update({n_coups : plat})
        plat = jouer_un_coup(plat,n)
        dissque_config(plat,n)
        #coups[n_coups] = {}
        #coups[n_coups]['Tour_1'] = plat[0]
        #"coups[n_coups]['Tour_2'] = plat[1]
        #coups[n_coups]['Tour_3'] = plat[2]
        
        dict2 = {n_coups : { 'Tour_1' : plat[0],
                              'Tour_2' : plat[1],
                              'Tour_3' : plat[2],
                             }
                }
        coups = merge(coups, dict2)
        #coups = dict(coups)
        #coups[n_coups] = plat

        print(coups)
        annuler = str(input("Voulez-vous annuler ce coup ? (o/n)"))
        if(annuler == "o") :
            n_dernier = list(coups.keys())[-1]
            coups = annuler_dernier_coup(coups, n_dernier)
            n_dernier = list(coups.keys())[-1]
            plat = [coups[n_dernier]['Tour_1'], coups[n_dernier]['Tour_2'], coups[n_dernier]['Tour_3']]
            victoire= False
        else :
            if (plat != [[],[],[]]) :
                 victoire = verifier_victoire(plat,n)
                 n_coups+=1
            else :
                  break
   
  return [n_coups-1, victoire]
    
    
    
  

 
