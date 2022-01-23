import time
import pickle
import turtle



start_time = time.time()


#---------------------------------------------
# Initialisation
#---------------------------------------------
plateau=[[],[],[]]
i=1



#---------------------------------------------
# Demander le nombre de disques
#---------------------------------------------


dictionnaire_score = {}
i=0
#---------------------------------------------
# Executer les fonctions de dernière partie (C)
#---------------------------------------------
exec(open('C:/Users/ibrah/Documents/Presentation_Python/Partie_C.py').read())
exec(open('C:/Users/ibrah/Documents/Presentation_Python/Partie_E.py').read())


while (i<2) :
    turtle.speed(300)
    turtle.hideturtle()
    start_time = time.time()
    print(" Bienvenue dans les Tours de Hanoi ")
    n=int(input(" Entrez le nombre de disques : "))
    j = 1
    plateau=[[],[],[]]
    while j<=n:
       plateau[0].insert(0,j)
       j+=1
#---------------------------------------------
# Executer la boucle du jeu (partie C & D)
#---------------------------------------------
    donnees = boucle_jeu(plateau,n)



#---------------------------------------------
# Enregistrer les données (partie E)
#---------------------------------------------



    if(donnees[1]) :
        print("Félicitations !")
        nom = str(input("Ecrire votre nom :"))
        dictionnaire_score[nom] = {}
        dictionnaire_score[nom]["nb_disque"] = n
        dictionnaire_score[nom]["nb_coups"] = donnees[0]
        dictionnaire_score[nom]["time"] = time.time() - start_time


        # creation du fichier Pickle 
        pickle_out = open("Scores_Des_Joueurs.pickle","wb")
        pickle.dump(dictionnaire_score, pickle_out)
        pickle_out.close()
    turtle.clearscreen()
    i+=1


#Lecture du fichier 
pickle_in = open("Scores_Des_Joueurs.pickle","rb")
example_dictio = pickle.load(pickle_in)


# Dictionnaire des scores
print(example_dictio)

# Meilleurs scores (nombre de coups)
afficher_meilleurs_scores(example_dictio) 

# Temps moyen de reflexion
temps_moyen(example_dictio)

# Les joueurs les plus rapides
afficher_meilleurs_temps(example_dictio)


#print(jouer_un_coup([[3,2],[],[1]],3))

#print(efface_disque(2,[[3,2],[],[1]],3))


#dissque_config([[3,2],[],[1]],3)

#turtle.Screen()