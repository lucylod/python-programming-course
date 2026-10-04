
def letterCombinations(digits):
    telefon_tastatur = {
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    if digits == "":
        return []

    result = [""]

    for digit in digits:
        neue_liste = []
        letters = telefon_tastatur[int(digit)]  
        for combination in result:
            for letter in letters:              
                neue_liste.append(combination + letter)

        result = neue_liste

    return result


eingabe = input("Gib Ziffern von 2-9 (höchstens 4 erlaubt!): ")
ergebnis = letterCombinations(eingabe)
print(ergebnis)
