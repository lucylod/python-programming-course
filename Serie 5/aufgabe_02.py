def primes(n):
    primzahlen =[]
    for k in range(2, n+1):
        primzahl = True
        for d in range(2,k):
            if k%d==0:
                primzahl=False
        if primzahl:
                primzahlen.append(k)
    return primzahlen

def pfz(n):
    primzahlen = primes(n)
    faktoren={}
    for p in primzahlen: # wie oft ist p in n enthalten?
        exponent = 0
        for _ in range(n):
            if n%p == 0: #wenn n durch p teilbar ist
                n = n//p #diviere dann n durch p und erhöhe den zähler für die potenz
                exponent +=1

        if exponent > 0: #speichere p mit seinem exponenten
            faktoren[p] = exponent  

    return faktoren
                 
print(pfz(10))       
 