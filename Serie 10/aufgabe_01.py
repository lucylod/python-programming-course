<import numpy as np
import matplotlib.pyplot as plt

class Polynom:

    def __init__(self, coeffs):
        self.coeffs=coeffs

        
    def __mul__(self,other):

        if not isinstance(other,Polynom):
            raise TypeError("Multiplikation ist nur mit einem Polynom-Objekt erlaubt.")

        if len(self.coeffs) == 0 or len(other.coeffs) == 0:
            raise ValueError("Polynome dürfen nicht leer sein.")

        result= [0]*(len(self.coeffs)+len(other.coeffs)-1)


        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i+j] += self.coeffs[i] * other.coeffs[j]

        return Polynom(result)

    def __call__(self, x):
        """Ermöglicht p(x)."""
        y = 0
        for i, a in enumerate(self.coeffs):
            y += a * x**i
        return y


    def plot(self, x_1, x_2):
        """Plottet das Polynom im Intervall [x_1, x_2]."""
        x = np.linspace(x_1, x_2, 400)
        y = self(x)


        plt.figure()
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("p(x)")
        plt.title("Plot des Polynoms")
        plt.grid(True)
        plt.show()
   


p = Polynom([1, 2])
q = Polynom([3, 4, 5])
r = p * q
print(r.coeffs)

r.plot(-10,10)