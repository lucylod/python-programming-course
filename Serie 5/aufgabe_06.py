def collatz(n, m):
    folge = [n]
    k = None

    for i in range(1, m):
        ci = folge[-1]
        if ci % 2 == 0:
            ci_next = ci // 2
        else:
            ci_next = 3 * ci + 1
        folge.append(ci_next)
        if ci_next == 1 and k is None:
            k = i

    return folge, k

n = int(input("Gib die Startzahl n ein: "))
m = int(input("Gib die Anzahl der Elemente m ein: "))

folge, k = collatz(n, m)
print("Collatz-Folge:", folge)
if k is not None:
    print("Erste 1 an Index:", k)
else:
    print("1 erscheint in den ersten", m, "Elementen nicht")
