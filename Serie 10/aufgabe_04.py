import numpy as np
import matplotlib.pyplot as plt

# --- Funktion und Ableitung für Aufgabe 4 ---

def f(x):
    return x**3 - x - 2

def fprime(x):
    return 3*x**2 - 1


# --- Bisektionsverfahren: gibt Liste der x_i zurück ---

def bisection_sequence(f, a, b, tol=1e-10, max_iter=50):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) und f(b) müssen unterschiedliche Vorzeichen haben.")

    xs = []  # Liste der Mittelpunkte

    for _ in range(max_iter):
        m = 0.5 * (a + b)   # Mittelpunkt
        xs.append(m)

        if abs(f(m)) < tol or abs(b - a) < tol:
            break

        # Vorzeichenprüfung
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return xs


# --- Newtonverfahren: gibt Liste der x_i zurück ---

def newton_sequence(f, fprime, x0, tol=1e-10, max_iter=50):
    x = x0
    xs = [x]

    for _ in range(max_iter):
        fx = f(x)
        dfx = fprime(x)

        if abs(dfx) < 1e-14:
            raise ValueError("Ableitung fast 0, Newton bricht ab.")

        x_new = x - fx/dfx
        xs.append(x_new)

        x = x_new

        if abs(f(x)) < tol:
            break

    return xs


# --- Folgen berechnen ---

# Bisection auf [1, 3]
xs_bis = bisection_sequence(f, 1, 3, tol=1e-10, max_iter=50)

# Newton mit Startwert x0 = 2
xs_newt = newton_sequence(f, fprime, 2.0, tol=1e-10, max_iter=50)

# Iterationsnummern
its_bis = np.arange(len(xs_bis))
its_newt = np.arange(len(xs_newt))

# |f(x_i)| berechnen
errs_bis = [abs(f(x)) for x in xs_bis]
errs_newt = [abs(f(x)) for x in xs_newt]


# --- Plot 1: normale y-Achse ---

plt.figure(figsize=(8, 5))
plt.plot(its_bis, errs_bis, "o-", label="Bisection")
plt.plot(its_newt, errs_newt, "s-", label="Newton")

plt.xlabel("Iteration i")
plt.ylabel("|f(x_i)|")
plt.title("Konvergenzvergleich (normale Skala)")
plt.grid(True)
plt.legend()
plt.show()


# --- Plot 2: logarithmische y-Achse ---

plt.figure(figsize=(8, 5))
plt.plot(its_bis, errs_bis, "o-", label="Bisection")
plt.plot(its_newt, errs_newt, "s-", label="Newton")

plt.xlabel("Iteration i")
plt.ylabel("|f(x_i)| (log-skaliert)")
plt.title("Konvergenzvergleich (logarithmische Skala)")
plt.yscale("log")   # <- hier wird die y-Achse logarithmisch gemacht
plt.grid(True, which="both")
plt.legend()
plt.show()
