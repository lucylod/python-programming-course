import numpy as np
import time
import matplotlib.pyplot as plt


#matrixgrößen

n_values=[50,100,200,400,800]
times=[]

for n in n_values:
    A=np.random.rand(n,n)
    B=np.random.rand(n,n)

    start = time.time()
    C= np.dot(A,B)
    end=time.time()

    times.append(end-start)
    print(f"n={n},Zeit={end-start:.6f}s")
    

#log-log-Plot

plt.figure()
plt.loglog(n_values, times, marker="o")
plt.xlabel("Matrixgroße n")
plt.ylabel("Rechenzeit [s]")
plt.title("Aufwand der Matrix-Matrix-Multiplikation")
plt.grid(True)
plt.show()

