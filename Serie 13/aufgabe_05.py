"""Anforderungen:
1. LinearFunktion und QuadraticFunktion erben von Polynom
2. Konstrukturen nehmen einzelne Koeffizienten, nicht Listen
3. Jede Klasse hat eine Methode roots() -> Liste der reellen Nullstellen
4. __add__ und __sub__ sollen Objekte der passenden Klasse zurückgeben
z.B kann die Summe zweier Auadratischer linear oder konstant sein
"""
import math

class Polynom:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # coefficients are in increasing order of power

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))
    
    def __add__(self, other):
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 + coef2)
        return Polynom(new_coeffs)
    def __sub__(self, other):
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 - coef2)
        return Polynom(new_coeffs)
    



"""
for i in range(len(self.coefficients)-1,-1,-1):
range(start,stop,step)
start = len(...)-1 -> letzter index
stop=-1 -> bis Index 0 (exklusiv)
step=-1 -> rückwärts zählen 
    """

    def degree(self):
        for i in range(len(self.coefficients)-1,-1,-1):
            if self.coefficients[i]!=0
                return i
            return 0
        
class LinearFunction(Polynom):
    def __init__(self,a0,a1):
        super().__init__([a0,a1])


        def roots(self):
            a0,a1=self.coefficients
            if a1 == 0:
                return []
            
            return [-a0/a1]




    
