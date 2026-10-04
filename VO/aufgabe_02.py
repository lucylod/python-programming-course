a=input("Geben Sie eine Zahl für a ein.")
b=input("Geben Sie eine Zahl für b ein.")
c=input("Geben sie eine Zahl für c ein.")


def sort3(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    zahlen=[a,b,c]
    zahlen.sort(reverse=True)
    print(zahlen)
    return zahlen 
   
sort3(a,b,c)
