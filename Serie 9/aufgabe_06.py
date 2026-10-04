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


p = Polynom([1, 2])
q = Polynom([3, 4, 5])
r = p * q
print(r.coeffs)
