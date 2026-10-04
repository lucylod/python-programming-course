import numpy as np
import matplotlib.pyplot as plt


def monte_carlo_integral(f, a, b, n):
    """
    Monte-Carlo-Approximation des Integrals von f auf [a,b]
    """
    x = np.random.uniform(a, b, size=n)
    return (b - a) * np.mean(f(x))

def f(x):
    return x**2

exact_value = 1/3


n_values = [100, 300, 1000, 3000, 10000, 30000]
num_runs = 50

errors = []

for n in n_values:
    estimates = [
        monte_carlo_integral(f, 0, 1, n)
        for _ in range(num_runs)
    ]
    mean_estimate = np.mean(estimates)
    error = abs(mean_estimate - exact_value)
    errors.append(error)


plt.figure()
plt.loglog(n_values, errors, marker="o", label="Monte-Carlo-Fehler")

# Referenzlinie ~ 1/sqrt(n)
ref = errors[0] * np.sqrt(n_values[0] / np.array(n_values))
plt.loglog(n_values, ref, "--", label=r"$\sim 1/\sqrt{n}$")

plt.xlabel("Anzahl der Stichproben n")
plt.ylabel("Fehler")
plt.title("Monte-Carlo-Integration: Fehlerverhalten")
plt.legend()
plt.grid(True)
plt.show()
