def reverse_rows_shallow(matrix):
    neue_matrix=[]

    for i in range(len(matrix)-1,-1,-1):
        neue_matrix.append(matrix[i])
    return neue_matrix


def reverse_rows_copy(matrix):
    neue_matrix=[]

    for i in range(len(matrix)-1,-1,-1):
        neue_zeile=matrix[i].copy()
        neue_matrix.append(neue_zeile)
    return neue_matrix




# --- Eingabe ---

def eingabe():

    n_input = input("Wie viele Zeilen hat die Matrix?")
    if n_input.strip() == "" or not n_input.strip().isdigit():
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
        
        L.append([int(x) for x in teile_zeile])

    return L


M = eingabe()

M_shallow = reverse_rows_shallow(M)
M_copy    = reverse_rows_copy(M)

print("Original:", M)
print("Shallow:", M_shallow)
print("Copy:   ", M_copy)

# jetzt Original verändern
M[0][0] = 999

print("Nach Änderung im Original:")
print("Original:", M)
print("Shallow:", M_shallow)  # ändert sich mit!
print("Copy:   ", M_copy)     # bleibt gleich!



