import math

class Square:

    def __init__(self, A,C):

        self.A=A
        self.C=C

    def side_length(self):
        xA,yA=self.A
        xC,yC=self.C


        d=math.sqrt((xC-xA)**2+(yA-yC)**2)


        return d/math.sqrt(2)
    

    def vertices(self):
        xA,yA=self.A
        xC,yC=self.C

        mx= xA+0.5*(xC-xA)
        my= yA+0.5*(yC-yA)

        B=(-(mx-xA)+mx,my-yA+my)
        D=((mx-xA)+mx,-(my-yA)+my)

        return (self.A,B,self.C,D)

    def area(self):
        s=self.side_length()
        return s*s


sq = Square((1, 2), (5, 6))

print("Eckpunkte:", sq.vertices())
print("Seitenlänge:", sq.side_length())
print("Fläche:", sq.area())
