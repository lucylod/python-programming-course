class Solution:
    def __init__(self, s, numRows):
        self.s = s
        self.numRows = numRows

    def convert(self):
        s = self.s
        numRows = self.numRows

        if numRows == 1:
            return s

        # Dictionary für die Zeilen
        row_map = {row: "" for row in range(1, numRows + 1)}

        row = 1
        up = False   # False = nach unten, True = nach oben

        for letter in s:
            row_map[row] += letter

            # Richtungswechsel
            if row == 1:
                up = False
            elif row == numRows:
                up = True

            # Bewegung
            if up:
                row -= 1
            else:
                row += 1

        converted = ""
        for row in range(1, numRows + 1):
            converted += row_map[row]

        return converted

text = input("Gib einen Text ein: ")
rows = int(input("Gib die Anzahl der Zeilen (numRows) ein: "))

solver = Solution(text, rows)
print("Ergebnis:", solver.convert())