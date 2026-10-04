n1=int(input("Gib eine natürliche Zahl für n1 an"))
n2=int(input("gib eine natürliche Zahl für n2 an"))

if n1 < 0 or n2 <0:
    print("Mindestens eine der angegebenen Zahlen ist negativ.")

if n1==n2:
    print("Sie sind gleich groß")

if n2>n1:
    print("Die größere Zahl ist",n2)

else:
    if n1>n2:
        tmp = n1
        n1 = n2
        n2 = tmp
        print("Die größere Zahl ist:",n2)