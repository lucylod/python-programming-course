import math

class polynom:
    def __init__(self, coeffs):
        """
        coeffs: Liste [a0, a1, ..., an] für
                f(x) = a0 + a1 x + ... + an x^n
        """
        self.coeffs = list(coeffs)
        self.degree = len(self.coeffs) - 1

    # 1. Auswertung f(x)
    def eval(self, x):
        value = 0.0
        for k, a_k in enumerate(self.coeffs):
            value += a_k * (x ** k)
        return value

    # 2. Ableitung f'(x) als neues polynom-Objekt
    def diff(self):
        # Konstantes Polynom: Ableitung ist 0
        if self.degree == 0:
            return polynom([0])

        deriv_coeffs = []
        # k * a_k wird Koeffizient von x^(k-1)
        for k in range(1, self.degree + 1):
            deriv_coeffs.append(k * self.coeffs[k])
        return polynom(deriv_coeffs)

    # 3. Bestimmtes Integral \int_{x1}^{x2} f(x) dx
    def integrate(self, x1, x2):
        """
        Nutzt Stammfunktion:
        F(x) = a0 x + a1 x^2/2 + ... + an x^(n+1)/(n+1)
        und gibt F(x2) - F(x1) zurück.
        """
        # Koeffizienten der Stammfunktion F(x)
        F_coeffs = [0.0] * (self.degree + 2)  # Grad n+1 -> n+2 Koeffizienten
        for k, a_k in enumerate(self.coeffs):
            F_coeffs[k + 1] = a_k / (k + 1)

        F = polynom(F_coeffs)
        return F.eval(x2) - F.eval(x1)

    # 4. Nullstellen eines Polynoms 2. Grades
    def zeros(self):
        """
        Berechnet die Nullstellen eines Polynoms 2. Grades.
        - Wenn Grad != 2 -> ValueError
        - Wenn keine reellen Nullstellen -> None
        - Sonst liste der Nullstellen (eine oder zwei Zahlen)
        """
        if self.degree != 2:
            raise ValueError("zeros() ist nur für Polynome 2. Grades definiert.")

        a0, a1, a2 = self.coeffs[0], self.coeffs[1], self.coeffs[2]

        if a2 == 0:
            # Eigentlich kein Polynom 2. Grades, aber wir behandeln es kurz:
            # a1 x + a0 = 0 -> x = -a0 / a1
            if a1 == 0:
                # Konstant, entweder nie 0 oder immer 0
                return None
            return [-a0 / a1]

        # Diskriminante
        D = a1 ** 2 - 4 * a2 * a0

        if D < 0:
            return None
        elif D == 0:
            x = -a1 / (2 * a2)
            return [x]
        else:
            sqrtD = math.sqrt(D)
            x1 = (-a1 + sqrtD) / (2 * a2)
            x2 = (-a1 - sqrtD) / (2 * a2)
            return [x1, x2]

    # 5. Statische Methode: Summe zweier Polynome
    @staticmethod
    def add(f1, f2):
        """
        Addiert zwei Polynome f1 und f2 und gibt ein neues polynom zurück.
        """
        max_deg = max(f1.degree, f2.degree)
        sum_coeffs = []

        for k in range(max_deg + 1):
            c1 = f1.coeffs[k] if k <= f1.degree else 0
            c2 = f2.coeffs[k] if k <= f2.degree else 0
            sum_coeffs.append(c1 + c2)

        return polynom(sum_coeffs)


# --- einfache Tests ---

# f(x) = 1 + 2x + 3x^2
p = polynom([1, 2, 3])
print("p.coeffs =", p.coeffs, "degree =", p.degree)
print("p(2) =", p.eval(2))          # 1 + 4 + 12 = 17

# Ableitung: f'(x) = 2 + 6x
dp = p.diff()
print("p'(x) Koeffizienten =", dp.coeffs)
print("p'(2) =", dp.eval(2))        # 2 + 12 = 14

# Integral von f(x) von 0 bis 1
print("∫_0^1 p(x) dx ≈", p.integrate(0, 1))

# Quadratisches Polynom mit zwei Nullstellen: x^2 - 1
q = polynom([-1, 0, 1])
print("Nullstellen von q:", q.zeros())   # sollte ungefähr [-1, 1] sein

# Quadratisches Polynom ohne reelle Nullstellen: x^2 + 1
r = polynom([1, 0, 1])
print("Nullstellen von r:", r.zeros())   # sollte None sein

# Summe zweier Polynome
s = polynom.add(p, q)
print("p(x) + q(x) Koeffizienten =", s.coeffs)
