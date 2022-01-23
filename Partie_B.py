

#---------------------------------------------
# Executer les fonctions de la partie A
#---------------------------------------------

exec(open('C:/Users/ibrah/Documents/Presentation_Python/Partie_A.py').read())

#---------------------------------------------
# Executer les fonctions de la partie B
#---------------------------------------------


import turtle


def dessine_plateau(n):
  i=1
  s=209
  turtle.up()
  turtle.goto(-400,-200)
  turtle.down()
    
  while i<=2:
    turtle.color("black","Dark Turquoise")
    turtle.begin_fill()
    turtle.forward(s+(90*(n-1)))
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.end_fill()
    i+=1

  m=((n*30+10)/2)+20 
  l=m*2-20  
  a=(-400)+m
  b=a+l
  c=b+l
  

  turtle.up()
  turtle.goto(a,-180)
  turtle.down()
  
  i=1
  while i<=2:
    turtle.begin_fill()
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(20*(n+1))
    turtle.left(90)
    turtle.end_fill()
      
  
    i+=1
      
  turtle.up()
  turtle.goto(b,-180)
  turtle.down()

  i=1   
  while i<=2:
    turtle.begin_fill()
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(20*(n+1))
    turtle.left(90)
    turtle.end_fill()
    i+=1
  
  turtle.up()
  turtle.goto(c,-180)
  turtle.down()

  i=1
  while i<=2: 
    turtle.begin_fill()
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(20*(n+1))
    turtle.left(90)
    turtle.end_fill()
    i+=1

    
  
  return





def efface_disque(nd,plateau,n):
  m=((n*30+10)/2)+20  
  l=m*2-20  
  a=(-400)+m
  h=a+l
  c=h+l
  i=0
  turtle.color("white", "white")
  while i<len(plateau):
    if nd in plateau[i]:
        x=list(plateau[i])
        q=x.index(nd)
        z=-180+(q*20)
        a=i
        b=nd*30+10
        if a==0:
          turtle.up()
          turtle.goto(-377+15*(n-nd),z)
          turtle.down()
          i=1
          while i<=2: 
                turtle.begin_fill()
                turtle.forward(b)
                turtle.left(90)
                turtle.forward(20)
                turtle.left(90)
                turtle.end_fill()
                i+=1
                
     
        elif a==1:
          turtle.up()
          turtle.goto(h-((40+(nd-1)*30)/2)+3,z)
          turtle.down()
          i=1
          while i<=2: 
            turtle.begin_fill()
            turtle.forward(b)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.end_fill()
            i+=1
              
        elif a==2:
          turtle.up()
          turtle.goto(c-((40+(nd-1)*30)/2)+3,z)
          turtle.down()
          i=1
          while i<=2: 
            turtle.begin_fill()
            turtle.forward(b)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.end_fill()
            i+=1
                

    i+=1    
  #turtle.Terminator    
  return


def dessine_disque(nd,plateau,n):
  m=((n*30+10)/2)+20
  l=m*2-20  
  a=(-400)+m
  h=a+l
  c=h+l
  i=0
  turtle.color("black", "violet red")
  while i<len(plateau):
    if nd in plateau[i]:
        x=list(plateau[i])
        q=x.index(nd)
        z=-180+(q*20)
        a=i
        b=nd*30+10
        if a==0:
          turtle.up()
          turtle.goto(-377+15*(n-nd),z)
          turtle.down()
          i=1
          while i<=2: 
            turtle.begin_fill()
            turtle.forward(b)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.end_fill()  
            i+=1
             

        elif a==1:
          turtle.up()
          turtle.goto(h-((40+(nd-1)*30)/2)+3,z)
          turtle.down()
          i=1
          while i<=2: 
            turtle.begin_fill()
            turtle.forward(b)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.end_fill()  
            i+=1
       
        elif a==2:
          turtle.up()
          turtle.goto(c-((40+(nd-1)*30)/2)+3,z)
          turtle.down()
          i=1
          while i<=2: 
            turtle.begin_fill()
            turtle.forward(b)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.end_fill()  
            i+=1
    
    i+=1
  return


def dissque_config(plateau,n):
    i=0
    dessine_plateau(n)
    while i<3:
        a=list(plateau[i])
        j=0
        while j<len(a):
            nd=a[j]
            dessine_disque(nd,plateau,n)
            j+=1
        i+=1
    return 


def efface_tout(plateau,n):
    i=0
    while i<3:
        a=list(plateau[i])
        j=0
        while j<len(a):
            nd=a[j]
            efface_disque(nd,plateau,n)
            j+=1
        i+=1
    return 


