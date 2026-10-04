def determinante(matrix):
    for row in matrix:
        if len(row) != len(matrix):
            print("Fehler: Matrix ist nicht quadratisch!")
            return None
      
    n = len(matrix)

    if n==1:
        return matrix[0][0]
    

    det=0


    for j in range(n):
        wert=matrix[0][j]
        unter=[row[:j]+row[j+1:]for row in matrix[1:]]
        det_unter=determinante(unter)
        vorzeichen=(-1)**j
        det += vorzeichen * wert * det_unter

    return det




# --- Eingabe ---

def eingabe():

    n_input = input("Wie groß ist die Matrix? (z.B. 3 für 3x3): ")
    if not n_input.strip().isdigit():
        print("Fehler: Keine gültige Zahl für n.")
        return
    
    n=int(n_input)

    L=[]

    print("Gib die Matrixzahlen an (jeweils mit Kommas trenen!):")
    for i in range(n):
        zeile=input(f"Zeile{i+1}:")
        teile_zeile = zeile.split(",")

        if zeile.strip()== "" or not all(t.strip().lstrip("-").isdigit() for t in teile_zeile):
            print("Fehler: Keine gültige Eingabe.")
            return
        
        L.append([int(x) for x in zeile.split(",")])

    ergebnis = determinante(L)
    print("Die Determinante ist:", ergebnis)

eingabe()




    



    




