a = float(input("Gib eine Zahl für den ersten Parameter an."))
b = float(input("Gib eine Zahl für den zweiten Parameter an."))
c = float(input("Gib eine Zahl für den dritten Parameter an."))

def mittelwert(a,b,c):
   parameter = [a,b,c]
   return sum(parameter)/len(parameter)


ergebnis=(mittelwert(a,b,c))


def standardabweichung(a,b,c):
   parameter = [a,b,c]
   return sum((x-ergebnis)**2 for x in parameter)/(len(parameter)-1)


print(f"Der Mittelwert berägt: {mittelwert(a,b,c):.2f}")
print(f"Die Standardabweichung berägt:{standardabweichung(a,b,c):.2f}")