import time
import random
import math


def merge(l1, l2):
    ergebnis=[]
    i=0
    j=0
    while i < len(l1) and j<len(l2):
        akt1=l1[i]
        akt2=l2[j]

        if akt1 <= akt2:
            ergebnis.append(akt1)
            i+=1

        else:
            ergebnis.append(akt2)
            j+=1
    
    while i<len(l1):
        ergebnis.append(l1[i])
        i+=1
    
    while j<len(l2):
        ergebnis.append(l2[j])
        j+=1

    return ergebnis



def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    # wir erstellen zwei unterlisten

    

    mid=int(len(lst)//2)
    l=lst[:mid]
    r=lst[mid:]

    left_sorted=merge_sort(l)
    right_sorted=merge_sort(r)

    return merge(left_sorted,right_sorted)

    

    
#bonus

print("k    n=2^k        Zeit [s]    Zeit/n         Zeit/(n*log2 n)")
print("-------------------------------------------------------------")

for k in range(10,21):
    n=2**k

    lst = [random.randint(0, 1000000) for _ in range(n)]
    
    start= time.time()
    merge_sort(lst)
    end=time.time()

    t=end-start

    print(f"{k:<2} {n:<10}  {t:>9.6f}  {t/n:>11.8f} {t/(n*math.log2(n)):>14.8f}"

    )

