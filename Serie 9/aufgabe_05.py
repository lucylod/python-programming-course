def back_substitution(U,b):
    n=len(b)
    
    #Prüfen auf Langzeitfehler


    if n==0:
        raise ValueError("Vektor b darf nicht leer sein.")
    
    #prüfen ob U die richtige Anzahl Zeilen hat

    if len(U)!=n:
        raise ValueError("U muss genauso viele Zeilen haben wie b Einträge haben.")
    
    
    #prüfen ob U quadratisch ist

    for row in U:
        if len(row) !=n:
            raise ValueError("U muss eine quadratische Matrix sein.")


    # algorithmus
    x=[0.0]*n
    x[n-1]=b[n-1]/U[n-1][n-1]


    for i in range(n-2,-1,-1):
        summe=0.0

        for j in range(i+1,n):
            summe+=U[i][j]*x[j]

        x[i]=(b[i]-summe)/U[i][i]

    return x


U = [
    [2, 1, -1],
    [0, 3, 2],
    [0, 0, 4]
]

b = [1, 5, 8]

x = back_substitution(U, b)
print(x)



