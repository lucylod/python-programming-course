import

class MyVector2d:

    def __init__(self, x, y):

        self.x=x
        self.y=y


    def print(self):
        print(f"({self.x}, {self.y})")

    
    def length(self):
        return math.sqrt(self.x**2)



