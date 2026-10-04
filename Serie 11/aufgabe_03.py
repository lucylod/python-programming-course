import time
import matplotlib.pyplot as plt



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quicksort(left) + middle + quicksort(right)

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = quicksort(data)
print("Sorted array using quicksort:", sorted_data)


def measure_time(arr):
    start = time.perf_counter()
    quicksort(arr)
    end = time.perf_counter()
    return end - start


sizes = [100, 200, 400, 800, 1600]
times = []

for n in sizes:
    data = [1] * n   # Worst Case
    t = measure_time(data)
    times.append(t)
    print(f"n={n}, time={t:.6f}s")


plt.figure()
plt.plot(sizes, times, marker='o')
plt.xlabel("Eingabegröße n")
plt.ylabel("Laufzeit in Sekunden")
plt.title("QuickSort Worst Case (O(n²))")
plt.grid(True)
plt.show()
