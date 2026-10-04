def quersumme(z):
    summe = 0
    for index, stelle in enumerate(str(z)):
       print("stelle",index +1, "=", stelle)
       summe = summe + int(stelle)
    return summe


zahl = int(input("Gib eine Zahl ein:"))
qs=quersumme(zahl)
print(qs)

