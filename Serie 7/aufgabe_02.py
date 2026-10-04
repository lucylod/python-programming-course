list1=[]
list2=[]

def merge(l1, l2):
    ergebnis=[]
    i=0
    j=0
    while i < len(l1) and j<len(l2):
        akt1=l1[i]
        akt2=l2[j]

        if akt1 <= akt2:
            ergebnis.append(akt1)
            i+=1

        else:
            ergebnis.append(akt2)
            j+=1
    
    while i<len(l1):
        ergebnis.append(l1[i])
        i+=1
    
    while j<len(l2):
        ergebnis.append(l2[j])
        j+=1

    return ergebnis


# -------- Eingabe ----------

eingabe1= input("Bitte Zahlen in aufsteigender Reihenfolge eingeben!")

for x in eingabe1.split(","):
    list1.append(int(x))


eingabe2= input("Bitte Zahlen in aufsteigender Reihenfolge eingeben!")

for x in eingabe2.split(","):
    list2.append(int(x))

print(merge(list1, list2))









