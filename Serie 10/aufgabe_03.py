import numpy as np
import matplotlib.pyplot as plt


def newton(f,fprime,x0,tol):
    x=x0

    while True:

        if abs(fprime(x))<=tol*abs(f(x)):
            raise ValueError("Newton-Abbruch: Ableitung zu klein.")     
        
        x_former=x
        x_new=x-(f(x)/fprime(x))
        x=x_new
        
        if abs(f(x))<tol or abs((x-x_former))<tol:
            return x
        
result = newton(lambda x: x**2-2,
                lambda x:2*x,
                1,
                1e-6)

print(result)
        


import numpy as np
import matplotlib.pyplot as plt

def newton_visualize(f, fprime, x0, tol, max_iter=6):
    x = x0

    # ein einmaliger Schritt, um |x0 - x1| zu bestimmen
    x1 = x0 - f(x0)/fprime(x0)
    step_size = abs(x0 - x1)

    for k in range(max_iter):

        fx = f(x)
        dfx = fprime(x)

        # Newton-Schritt
        x_next = x - fx/dfx

        # Intervall berechnen
        left = x - 1.5 * step_size
        right = x + 1.5 * step_size
        xs = np.linspace(left, right, 600)
        
        # Funktion auswerten
        ys = f(xs)

        # Tangente T(x) = f(x_k) + f'(x_k)(x - x_k)
        tangent = fx + dfx * (xs - x)

        # Plot
        plt.figure(figsize=(9, 5))

        # Funktion
        plt.plot(xs, ys, label="f(x)")

        # Punkt (x_k, f(x_k))
        plt.scatter([x], [fx], color="blue", zorder=5, label="(x_k, f(x_k))")

        # Tangente
        plt.plot(xs, tangent, "--", color="green", label="Tangente")

        # Schnittpunkt mit x-Achse
        plt.scatter([x_next], [0], color="red", zorder=5, label="x_{k+1}")

        # x-Achse
        plt.axhline(0, color="black", linewidth=1)

        plt.title(f"Newton-Schritt {k}: x_k = {x:.6f}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()

        plt.show()

        # nächstes x
        x = x_next
        
        # Abbruchbedingung wie in deinem Newton
        if abs(f(x)) < tol:
            break


def f(x):
    return x**2 - 2

def fprime(x):
    return 2*x


newton_visualize(f, fprime, x0=3, tol=1e-6, max_iter=5)
