def LxV(L, vector):
    n=len(L) #zählt, wie viele Zeilen die Matrix hat
    if len(vector)!=n:
        print("Der Vektor V hat nicht die gleiche Länge wie die Matrix L")
        return 

    for i in range(n): #gehen jede Zeile der matrix durch
        if len(L[i])!=n: #prüfen, ob die i-te Zeile gleich n ist
            print("Fehler: Matrix L ist nicht quadratisch!")
            return
 

    y=[0]*n #erstelle eine liste mit n Einträgen und fülle sie alle mit 0

    for i in range(n): 
        s=0             #summe am anfang jeder zeile 0 setzen
        for j in range(i+1): 
            s=s+L[i][j]*vector[j]
        y[i]=s

    return y


# --- Eingabe ---

def eingabe():

    vector_input=input("Gib die Werte des Vektors ein")
    teile= vector_input.split(",")

    if vector_input.strip() == "" or not all(t.strip().lstrip("-").isdigit() for t in teile):
        print("Fehler: Keine gültige Eingabe")
        return


    v = [int(x) for x in vector_input.split(",")]

   
    n=len(v)
    L=[]

    print("Gib die Matrixzahlen an (jeweils mit Kommas trenen!):")
    for i in range(n):
        zeile=input(f"Zeile{i+1}:")
        teile_zeile = zeile.split(",")

        if zeile.strip()== "" or not all(t.strip().lstrip("-").isdigit() for t in teile_zeile):
            print("Fehler: Keine gültige Eingabe.")
            return
        
        
        
        L.append([int(x) for x in zeile.split(",")])




    ergebnis = LxV(L, v)
    print("Ergebnis:", ergebnis)


eingabe()