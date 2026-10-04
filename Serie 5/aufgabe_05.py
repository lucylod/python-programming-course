def gewinner(position):
    for zeile in position:
        if zeile[0] == zeile[1] == zeile[2] != "":
            return zeile[0] + " gewinnt" 
    for spalte in range(3):
        if position[0][spalte] == position[1][spalte] == position[2][spalte] != "":
            return position[0][spalte] + " gewinnt"
    if position[0][0] == position[1][1] == position[2][2] != "": #überprüfung der hauptdiagona
        return position[0][0] + " gewinnt"
    if position[0][2] == position[1][1] == position[2][0] != "": #überprüfung der nebendiagonale
        return position[0][2] + " gewinnt"
    alle_felder = [feld for zeile in position for feld in zeile]
    if "" not in alle_felder:
        return "Unentschieden"
    return "Kein Gewinner"



position = []

print("Gib die Tic-Tac-Toe-Position ein (nur X oder O).")

for i in range(3):
    zeile = []
    for j in range(3):
        feld = input(f"Feld [{i+1},{j+1}]: ")
        while feld not in ["X", "O"]:
            feld = input("Bitte nur X oder O eingeben: ")
        zeile.append(feld)
    position.append(zeile)

print(gewinner(position))




position1 = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

position2 = [
    ["O", "X", "X"],
    ["O", "X", ""],
    ["O", "", ""]
]

position3 = [
    ["X", "O", "X"],
    ["O", "O", "X"],
    ["X", "X", "O"]
]

position4 = [
    ["X", "", "O"],
    ["", "O", "X"],
    ["", "", ""]
]

print(gewinner(position1))
print(gewinner(position2))
print(gewinner(position3))
print(gewinner(position4))


