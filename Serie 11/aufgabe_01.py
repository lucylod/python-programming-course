import random
import time
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def measure_time(n):
    # Zufällige Liste erzeugen
    data = [random.randint(0, 100000) for _ in range(n)]
    
    start = time.perf_counter()
    bubble_sort(data)
    end = time.perf_counter()
    
    return end - start


#testgrößen

sizes = [100, 200, 400, 800, 1600]
times = [] #speichert die gemessenen laufzeiten



for n in sizes:
    t = measure_time(n)
    times.append(t)
    print(f"n = {n:4d}, Zeit = {t:.6f} Sekunden")

plt.figure()
plt.plot(sizes, times, marker='o')
plt.xlabel("Eingabegröße n")
plt.ylabel("Laufzeit in Sekunden")
plt.title("Laufzeit von BubbleSort")
plt.grid(True)
plt.show()
