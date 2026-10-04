import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

N = 8                      # wie im Skriptum: n = 2^k
times = []
sizes = []

for k in range(N):
    n = 2**k
    data = [random.random() for _ in range(n)]

    start = time.time()
    bubble_sort(data)
    end = time.time()

    sizes.append(n)
    times.append(end - start)



plt.loglog(sizes, times, marker='o', label='BubbleSort')
plt.loglog(sizes, [1e-7*n*n for n in sizes],
           linestyle='dashed', label='O(n²)')
plt.xlabel("Problemgröße n")
plt.ylabel("Zeit (Sekunden)")
plt.legend()
plt.grid(True)
plt.show()

