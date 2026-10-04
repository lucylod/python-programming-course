# -------- Eingabe ----------

tuerme=[[],[],[]]



n=int(input("Wie viele Scheiben?"))

tuerme[0]=list(range(n,0,-1))

print("Startzustand:", tuerme)


# -------- Funktion ----------

def move(tuerme,Startstab,Zielstab):

    scheibe=tuerme[Startstab].pop()
    tuerme[Zielstab].append(scheibe)
    print("Bewege Scheibe von",Startstab+1,"zu",Zielstab+1)

    

def hanoi(m,Start, Ziel, Hilfe, tuerme):

    if m==1:
        move(tuerme,Start,Ziel)

    else:
        
        hanoi(m-1, Start, Hilfe,Ziel, tuerme)
        
        move(tuerme,Start,Ziel)

        hanoi(m-1,Hilfe, Ziel,Start,tuerme)
    

hanoi(n,0,2,1,tuerme)
  
print("Endzustand:", tuerme)    
           
           




