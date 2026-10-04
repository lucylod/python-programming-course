import random

def wuerfelsumme(n):
    return sum([random.randint(1,6) for _ in range(n)])


tausend=list()
[tausend.append(wuerfelsumme(2)) for _ in range (1000)]

dictionary={i:0 for i in range(2,13)}
for i in tausend:
    dictionary[i] += 1
    
max_key=max(dictionary,key=dictionary.get)
print(max_key,dictionary[max_key])

