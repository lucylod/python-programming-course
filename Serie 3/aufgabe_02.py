a= float(input("Gebe eine Zahl a die größer als 0 ist an: "))
b= float(input("Gebe eine Zahl b die größer als 0 ist an: "))
c= float(input("Gebe eine Zahl c die größer als 0 ist an: "))

if a<=0 or b<=0 or c<=0:
    print("Die Zahl muss größer als 0 sein!")

elif c>a and c>b: 
    hypotenuse = c
    katheten = (a,b)

elif a>c and a>b:
    hypotenuse = a
    katheten=(b,c)

else:
    hypotenuse = b
    katheten=(a,c)

if katheten[0]== katheten[1] and hypotenuse != katheten[0] or katheten[0] == hypotenuse and hypotenuse != katheten[1] or katheten[1] == hypotenuse and hypotenuse != katheten[0]:
    print("Das Dreieck ist gleichschenkelig")

elif katheten[0]==katheten[1]== hypotenuse:
    print("Das Dreieck ist gleichseitig")

elif abs(katheten[0]**2+katheten[1]**2==hypotenuse**2):
    print("Das Dreieck ist rechtwinkelig.")

elif katheten[0]+katheten[1] == hypotenuse:
    print("Das Dreieck ist ein eindimensional entartetes Dreieck.")

elif hypotenuse > katheten[0]+katheten[1]:
    print("Das Dreieck ist ein umögliches Dreieck.")

else: 
    print("Das Dreieck ist ein unregelmäßiges Dreieck.")









    

