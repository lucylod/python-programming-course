def probability(n, k):
    total = 1
    for d in range(1, n + 1):
        total *= (d + 1)

    # Kleinste und größte mögliche Summe
    min_sum = n
    max_sum = sum(range(2,n+2))

    if k < min_sum or k > max_sum:
        return 0.0

    # sum_counts[s] = wie viele Kombinationen ergeben die Summe s
    sum_counts = [0] * (max_sum + 1)
    sum_counts[0] = 1  # mit 0 Würfeln: genau eine Möglichkeit für Summe 0

    for d in range(1, n + 1):
        m = d + 1          # Seitenzahl des aktuellen Würfels (1..m)
        new_counts = [0] * (max_sum + 1)

        for s in range(max_sum + 1):
            if sum_counts[s] > 0:
                for v in range(1, m + 1):
                    if s + v <= max_sum:
                        new_counts[s + v] += sum_counts[s]

        sum_counts = new_counts

    ways = sum_counts[k]
    return ways / total


print(probability(2, 3))
