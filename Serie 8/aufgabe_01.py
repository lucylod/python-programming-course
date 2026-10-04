def sieve_of_eratosthenes(n):
    list_of_primes=[]
    for i in range(2,n+1):
        list_of_primes.append(i)
    

    for i in list_of_primes.copy():
        for j in range(2*i,n+1,i):
                if j in list_of_primes:
                    list_of_primes.remove(j)

    return list_of_primes


n=int(input("Gib eine Zahl ein:"))
result = sieve_of_eratosthenes(n)
print(result)   


    