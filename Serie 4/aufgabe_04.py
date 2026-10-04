from math import sqrt

phi= ((1+sqrt(5))/(2))

 
fib=[round(((phi**n -(-phi)**(-n)))/(sqrt(5))) for n in range(20)]


#es wird geprüft ob jede Zahl die summe der beiden vorhergehenden ist
check = all(fib[i]==fib[i-1]+fib[i-2] for i in range(2,20))
print(fib)
print("Summe-Prüfung korrekt:", check)

