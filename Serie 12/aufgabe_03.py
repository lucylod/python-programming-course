import numpy as np
import time
import matplotlib.pyplot as plt

#Strassen Algorithmus


def strassen(A,B):
    n=A.shape[0]

    if n<=2:
        return A @ B
    
    mid=n//2
    A11=A[:mid,:mid]
    A12=A[:mid, mid:]
    A21=A[mid:,:mid]
    A22=A[mid:, mid:]

    B11=A[:mid,:mid]
    B12=A[:mid, mid:]
    B21=A[mid:,:mid]
    B22=A[mid:, mid:]

    #Strassen-Hilfsmatrizen

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)
    
    C11=M1+M4-M5+M7
    C12=M3+M5
    C21=M2+M4
    C22=M1-M2+M3+M6

    C=np.vstack((np.hstack((C11,C12)),
                np.hstack((C21,C22)),

    ))

    return C


n_values=[32,64,128,256]
times=[]

for n in n_values:
    A=np.random.rand(n,n)
    B=np.random.rand(n,n)

    start=time.time()
    C=strassen(A,B)
    end=time.time()

    times.append(end-start)
    print(f"n={n}, Zeit={end-start:.6f}s")

plt.figure()

plt.loglog(n_values, times, marker="o", label="Messwerte")

# zwei Punkte auswählen: n = 64 und n = 128
i1, i2 = 1, 2

n1, n2 = n_values[i1], n_values[i2]
t1, t2 = times[i1], times[i2]

# Verbindungslinie
plt.plot([n1, n2], [t1, t2], "r--", linewidth=2, label="Verdopplung von n")

# Punkte hervorheben
plt.scatter([n1, n2], [t1, t2], color="red", zorder=5)

# Annotationen direkt im Plot
plt.annotate("n → 2n",
             xy=(n2, t1),
             xytext=(n1, t1),
             arrowprops=dict(arrowstyle="->"),
             fontsize=11)

plt.annotate("Zeit × ~7",
             xy=(n2, t2),
             xytext=(n2*1.05, t1*1.3),
             arrowprops=dict(arrowstyle="->"),
             fontsize=10)






plt.xlabel("Matrixgröße n")
plt.ylabel("Rechenzeit [s]")
plt.title("Strassen-Algorithmus: Laufzeit")
plt.grid(True)
plt.show()


    





