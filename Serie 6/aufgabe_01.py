from functools import cmp_to_key

def vergleichswort(wort1,wort2):
    vokale="aeiouAEIOU"
    anzahl1=sum(wort1.count(v) for v in vokale)
    anzahl2=sum(wort2.count(v) for v in vokale)

    if anzahl1>anzahl2:
        return 1
    
    elif anzahl1<anzahl2:
        return -1
    
    else:

        if wort1.lower() > wort2.lower():
            return 1
        
        elif wort1.lower() < wort2.lower():
            return -1
        
        else:
            return 0
        

eingabe = input("Gib eine Liste von Wörtern ein.")

wörter = [wort.strip() for wort in eingabe.split(",")]

sorted_list= sorted(wörter, key=cmp_to_key(vergleichswort))

print(sorted_list)