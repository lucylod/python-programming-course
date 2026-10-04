class MyComplex

    def __init__(self,real,imag):
        self.a=real
        self.b=imag

    def print(self):

        sign= "+" if self.b >=0 else "-"
        print(f"{self.a} {sign} {abs(self.b)}i")

    def conjugate(self):

        return MyComplex(self.a,-self.b)       

    @staticmethod
    def add(z1,z2):

        return MyComplex(z1.a + z2.a,z1.b+z2.b)
        


    @staticmethod
    def multiply(z1,z2):

        return MyComplex((z1.a*z2.b-z1.b*z2.b)+(z1.a*z2.b+z1.b*z2.a))
        
    def isReal(self):
            
        return self.b==0
        
    def isImaginary(self):
        return self.a ==0 and self.b !=0

            
real=float(input("Realteil eingeben:"))
imag=float(input("Imaginärteil eingeben:"))    

z=MyComplex(real,imag)
z.print()




