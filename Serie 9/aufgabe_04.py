class MyFunction:

    def __init__(self,f,a,b):
        self.f=f
        self.a=a
        self.b=b 


    #wir prüfen, ob der bereich gültig ist

        if a>b:
            raise ValueError("Ungültiger Definitionsbereich!")
    

    def __call__(self, x):

        if x<self.a or x>self.b:
            raise ValueError("x liegt nicht im Definitionsbereich!")
    
        return self.f(x)


#beispiele
f= MyFunction(lambda x:x**2,0,10)
print(f(3))
print(f(10))
print(f(-1))

