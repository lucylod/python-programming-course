def count_freq(values):
    """Zählt Häufigkeiten in einem Dictionary."""
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1
    return freq


def all_pairs():
    pairs = []
    for x in range(2, 100):
        for y in range(x + 1, 100):
            if x + y < 100:
                pairs.append((x, y))
    return pairs


def filter_step2(pairs):
    products = [x * y for x, y in pairs]
    freq_prod = count_freq(products)

    remaining = []
    excluded = []

    for p in pairs:
        prod = p[0] * p[1]
        if freq_prod[prod] > 1:
            remaining.append(p)
        else:
            excluded.append(p)

    return remaining, excluded


def filter_step3(pairs, excluded_step2):
    excluded_sums = set([x + y for (x, y) in excluded_step2])
    remaining = [p for p in pairs if (p[0] + p[1]) not in excluded_sums]
    return remaining


def filter_step4(pairs):
    products = [x * y for x, y in pairs]
    freq_prod = count_freq(products)

    remaining = [p for p in pairs if freq_prod[p[0] * p[1]] == 1]
    return remaining


def filter_step5(pairs):
    sums = [x + y for x, y in pairs]
    freq_sums = count_freq(sums)

    remaining = [p for p in pairs if freq_sums[p[0] + p[1]] == 1]
    return remaining


def lucifer_numbers():
    # Schritt 1
    pairs = all_pairs()

    # Schritt 2
    pairs_step2, excluded_step2 = filter_step2(pairs)

    # Schritt 3
    pairs_step3 = filter_step3(pairs_step2, excluded_step2)

    # Schritt 4
    pairs_step4 = filter_step4(pairs_step3)

    # Schritt 5
    pairs_step5 = filter_step5(pairs_step4)

    return pairs_step5


result = lucifer_numbers()
print("Übrig gebliebene Paare:", result)
