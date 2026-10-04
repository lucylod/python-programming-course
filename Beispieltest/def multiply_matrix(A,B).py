def multiply_matrix(A,B):

    if len(A[0])!=len(B):
        raise ValueError("Matrixmultiplikation nicht möglich!")
    
    result=[]

    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):

            summe=0
            
            for k in range(len(B)):
                summe += A[i][k]*B[k][j]
    
            row.append(summe)
        result.append(summe)    

    return result





    