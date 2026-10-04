import numpy as np

n = 4  # Beispielgröße

# Tridiagonalmatrix A

A = (4 * np.eye(n) #hauptdiagonale
    - np.eye(n, k=1) #obere den gnebendiagonale
    - np.eye(n, k=-1) #untere nebendiagonale
)

I = np.eye(n)           
Z = np.zeros((n, n))


blocks=[]

for i in range(n):

    row=[]

    for j in range(n):
        if i ==j:
            row.append(A)
        
        elif abs(i-j)==1:
            row.append(-I)

        else:
            row.append(Z)

    blocks.append(row)

C=np.block(blocks)

print("A =")
print(A)
print("\nC shape =", C.shape)