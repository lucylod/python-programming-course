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

print(primes(10))

