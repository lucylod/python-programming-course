class Matrix:
    def __init__(self,matrix):
        self.data = matrix 

        if not matrix:
            raise ValueError("Leere Matrix ist nicht erlaubt")
        
        #Prüfen, ob alle Zeilen gleich sind (rechteckig)
        
        row_length=len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise ValueError("Alle Zeilen müssen gleich lang sein")
        
        self.matrix=matrix #interne Matrix
        self.rows = len(matrix) #Anzahl der Zeilen
        self.cols = row_length #Anzahl der Spalten



    #WICHTIG: Addition ist nur erlaubt, wenn beide Matrizen gleich groß sind!
    def __add__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrixaddition nur bei gleichen Dimensionen möglich")
        
        result = []

        for i in range(self.rows):
            new_row=[]
            for j in range(self.cols):
                new_row.append(self.matrix[i][j] + other.matrix[i][j])


            result.append(new_row)

        return Matrix(result)

    def __mul__(self,other):
    
    #WICHTIG: Eine n x m Matrix kann nur mit einer m x k Matrix multipliziert werden
    
        if self.cols != other.rows:
            raise ValueError("Matrixmultiplikation nicht möglich")
        

        rows=self.rows
        cols=other.cols

        result=[]


        for i in range(self.rows):
            new_row=[]
            for j in range(other.cols):
                summe=0
                for k in range(other.rows):
                    summe+=self.matrix[i][k]*other.matrix[k][j]
                
                new_row.append(summe)

            result.append(new_row)
    
        return Matrix(result)
                 

A = Matrix([[1, 2, 3],
            [4, 5, 6]])

B = Matrix([[7, 8, 9],
            [1, 1, 1]])

C = A + B
print(C.matrix)

        

    
        





        
                









