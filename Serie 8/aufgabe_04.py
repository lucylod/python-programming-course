def contains_zero_bisection(x):
    """
    Prüft mit einem bisectionsähnlichen Verfahren,
    ob der Vektor x irgendwo die Zahl 0 enthält.
    Liefert:
      True  – 0 sicher gefunden
      False – 0 sicher nicht enthalten
      None  – Verfahren kann nicht eindeutig entscheiden
    """
    n = len(x)
    L, R = 0, n - 1

    while L <= R:
        mid = (L + R) // 2

        # direkt getroffen?
        if x[mid] == 0:
            return True

        # Schranken im linken Intervall [L, mid]
        dist_left = mid - L
        low_left = x[L] - dist_left #tiefste mögliche zahl von x
        high_left = x[L] + dist_left #höchste mögliche zahl an x
        left_possible = (low_left <= 0 <= high_left)

        # Schranken im rechten Intervall [mid, R]
        dist_right = R - mid
        low_right = x[R] - dist_right
        high_right = x[R] + dist_right
        right_possible = (low_right <= 0 <= high_right)

        # Entscheiden, welche Hälfte wir verwerfen können
        if left_possible and not right_possible:
            # 0 kann nur links liegen
            R = mid - 1
        elif right_possible and not left_possible:
            # 0 kann nur rechts liegen
            L = mid + 1
        elif not left_possible and not right_possible:
            # In keiner Hälfte möglich → 0 sicher nicht enthalten
            return False
        else:
            # In beiden Hälften möglich → Bisektionsidee versagt
            return None

    # Intervall leer, nichts gefunden
    return False


def contains_value_bisection(x, y):
    """
    Verallgemeinerung: prüft, ob ein bestimmter Wert y in x vorkommt.
    Wir suchen 0 in der Folge x[i] - y.
    """
    shifted = [xi - y for xi in x]
    return contains_zero_bisection(shifted)


# Beispiele:

# Fall, in dem das Verfahren gut funktioniert
v1 = [-3, -2, -1, 0, 1, 2]
print("v1 enthält 0? ->", contains_zero_bisection(v1))

# Fall, in dem 0 nicht enthalten ist
v2 = [-3, -2, -1, -1, -2, -3]
print("v2 enthält 0? ->", contains_zero_bisection(v2))

# Fall, in dem die Schranken kein eindeutiges Halbieren zulassen (None)
v3 = [1, 2, 1, 2, 1]  # erfüllt |x_{i+1}-x_i| <= 1, enthält aber keine 0
print("v3 enthält 0? ->", contains_zero_bisection(v3))

# Beispiel für allgemeines y
v4 = [2, 3, 4, 5, 6]
print("v4 enthält 4? ->", contains_value_bisection(v4, 4))
print("v4 enthält 10? ->", contains_value_bisection(v4, 10))
