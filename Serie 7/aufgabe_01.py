#rekursive funktion

recaman_list=[0]


def recaman(n):
    if n<0:
        return -1
    
    if n==0:
        return 0
    
    recaman(n-1)

    prev = recaman_list[n-1]
    candidate = prev-n


    if candidate > 0 and candidate not in recaman_list:
        recaman_list.append(candidate)

    else:
        recaman_list.append(prev+n)

    return recaman_list[n]


#nicht rekursive funktion

def recaman_iterativ(n):
    if n<0:
        return -1
    
    recaman_list =[0]

    for i in range(1,n+1):
        prev = recaman_list[i-1]
        candidate = prev - i

        if candidate > 0 and candidate not in recaman_list:
            recaman_list.append(candidate)

        else:
            recaman_list.append(prev + i)

    return recaman_list[n]
    
    

# -------- Eingabe ----------
n = int(input("Geben Sie n ein: "))
print("a_", n, "=", recaman(n), sep="")

