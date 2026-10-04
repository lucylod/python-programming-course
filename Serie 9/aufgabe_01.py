class MySet:

    def __init__(self,data):
        self.data=[]
        for x in data:
            if x not in self.data:
                self.data.append(x)

    def __add__(self,a):
        result=[]

        for x in self.data:
            result.append(x)

        for x in a.data:
            if x not in result:
                result.append(x)

        return MySet(result)
    
    def __sub__(self,a):
        result=[]

        for x in self.data:
            if x not in a.data:
                result.append(x)

        return MySet(result)

    def __str__(self):
        return "{"+", ".join(str(x) for x in self.data)+ "}"

eingabe = input("Gib Elemente ein: ")
liste = [int(x) for x in eingabe.split()]
m = MySet(liste)
print(m)


    
            





    


