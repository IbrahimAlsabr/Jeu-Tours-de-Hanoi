

def afficher_meilleurs_scores(dict_des_resultats) :
    #print (dict_des_resultats)
    dic_meilleurs_scores = {}
    for key, value in dict_des_resultats.items():
        for cles,valeurs in value.items():
            if(cles == "nb_coups") :
                dic_meilleurs_scores[key] = valeurs

    
    print(sorted(dic_meilleurs_scores.items(), key = lambda kv:(kv[1], kv[0]))) 

            #print (cles, valeurs)

        # print (key, value)
    return


def temps_moyen(dict_des_resultats) :
    dic_temps_moyen = {}
    for key, value in dict_des_resultats.items():
        for cles,valeurs in value.items():
            if(cles == "time") :
                dic_temps_moyen[key] = valeurs / dict_des_resultats[key]['nb_coups']
    
    print(dic_temps_moyen)
    return
    


def afficher_meilleurs_temps(dict_des_resultats) :
    #print (dict_des_resultats)
    dic_meilleurs_scores = {}
    for key, value in dict_des_resultats.items():
        for cles,valeurs in value.items():
            if(cles == "time") :
                dic_meilleurs_scores[key] = valeurs

    
    print(sorted(dic_meilleurs_scores.items(), key = lambda kv:(kv[1], kv[0]))) 

            #print (cles, valeurs)

        # print (key, value)
    return


