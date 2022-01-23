def Tour_Hanoi(n , tour_depart, tour_arrive, tour_auxiliare): 
    if n == 1: 
        print ("Deplacer le disque 1 de la tour",tour_depart,"a la tour",tour_arrive)
        return
    Tour_Hanoi(n-1, tour_depart, tour_auxiliare, tour_arrive) 
    print ("Deplacer le disque",n,"de la tour",tour_depart,"a la tour",tour_arrive )
    Tour_Hanoi(n-1, tour_auxiliare, tour_arrive, tour_depart)

# Driver code 
n = 3
Tour_Hanoi(n, 0, 2, 1)  