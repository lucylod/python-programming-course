import random
import time
import matplotlib.pyplot as plt



def merge(left, right):
    result = []
    i = j = 0

    # solange beide Listen noch Elemente haben
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # rest von left anhängen

    while i < len(left):
        result.append(left[i])
        i +=1

    
    # rest von right anhängen

    while j < len(right):
        result.append(right[j])
        j +=1

    return result


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 
    left = mergesort(arr[:mid]) #Aufwand A(n/2)
    right = mergesort(arr[mid:]) #Aufwand A(n/2)
    return merge(left, right) #Aufwand bn



import random
import time
import matplotlib.pyplot as plt


def measure_time(n):
    data = [random.randint(0, 100000) for _ in range(n)]

    start = time.perf_counter()
    mergesort(data)
    end = time.perf_counter()

    return end - start


sizes = [2**k for k in range(6, 15)]  # 64, 128, ..., 16384 (2^k wie in der Aufgabe)
times = []

for n in sizes:
    t = measure_time(n)
    times.append(t)
    print(f"n = {n:5d}, Zeit = {t:.6f} s")

plt.figure()
plt.plot(sizes, times, marker="o")
plt.xlabel("Eingabegröße n")
plt.ylabel("Laufzeit in Sekunden")
plt.title("Laufzeit von MergeSort")
plt.grid(True)
plt.show()
