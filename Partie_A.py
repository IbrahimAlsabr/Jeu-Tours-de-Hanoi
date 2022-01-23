# Partie A
# Question N°1
def init(n):
  plateau=[[],[],[]]
  i=0
  while i<n:
    j=1
    while n>=j:
      plateau[0].insert(i,n)
      n-=1
      i+=1
  return plateau

print(init(5))

# Question N°2
def nombre_disque(plateau,numtour):
  if numtour>2 or numtour<0:
    a="supposé incorrect"
  else:
    a=len(plateau[numtour])
  return a

#print(nombre_disque([[5,4,3],[2],[1]],1))

# Question N°3
def disque_superieur(plateau,numtour):
  if numtour>2 or numtour<0:
    max="supoosé incorrect"
  else:
    a=list(plateau[numtour])
    if a==[]:
      max=-1
    else:
      max=a[0]
  return max

#print(disque_superieur([[5,4],[3,2,1],[]],1))

# Question N°4
def position_disque(plateau,numdisque):
  i=0 
  while i<len(plateau):
    if numdisque in plateau[i]:
      position=i
    i+=1
  return position

#print(position_disque([[5,4],[3,2],[1]],4))


# Qustion N°5
def verifier_deplacement(plateau,nt1,nt2):
  if plateau[nt1]!=[] and plateau[nt2]==[]:
    return True 
  
  elif plateau[nt1]!=[] and plateau[nt2]!=[]:
    if disque_superieur(plateau,nt2) > disque_superieur(plateau,nt1):
      return True
    else:
      return False 

#print(verifier_deplacement([[6,5,4],[3],[2,1]],1,2))

#Question N°6
def verifier_victoire(plateau,n):
  i=0
  plateau1=[[],[],[]]
  while i<n:
    j=1
    while n>=j:
      plateau1[2].insert(i,n)
      n-=1
      i+=1
    if plateau1==plateau:
      a= True
    else:
      a=False
      
  return a

#print(verifier_victoire([[],[],[6,5,4,3,2,1]],6))

