import random

a = int(input("Gib die erste Zahl für a ein: "))
b = int(input("Gib die zweite Zahl für b ein: "))
c = int(input("Gib die dritte Zahl für c ein: "))

zahlen = [a, b, c]
n = random.randint(1, 10)

def pruefe_zahlen(zahlen, n):
    if n in zahlen:
        print("Die Zahl", n, "ist in der Liste enthalten!")
        zahlen.remove(n)
        
    else:
        print("\nDie Zahl", n, "ist nicht in der Liste enthalten.")
    return zahlen

zahlen = pruefe_zahlen(zahlen, n)

print("Liste:", zahlen)