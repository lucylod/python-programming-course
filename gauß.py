import numpy as np

#Gauß-Algorithmus für das LGS Ax=b


#Koeffizientenmatrix

a=np.array([[3,2,1],
            [1,2,3],
            [2,1,4]],dtype=float)


#Inhomogenitätsvektor

b=np.array([10,14,16],dtype=float)


def gauss(a,b):
#obere Dreiecksmatrix erzeugen

    a=a.copy()
    b=b.copy()

    n=len(b)

    for k in range(0,n): #Pivotindex (Diagonale)
        pivot=a[k,k]
        for i in range(k+1,n): #Zeilen unter der Pivotzeile
            f=a[i,k]/pivot
            b[i]=b[i]-f*b[k]

            for j in range(k,n): # Spalten

                a[i,j]=a[i,j]-f*a[k,j]

            print(a)

    #Rücksubstitution 

    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        s=0.0
        for j in range(i+1,n):
            s+= a[i,j]*x[j]
        
        x[i]=(b[i]-s)/a[i,i]

        return x



print("Inhomogenitätsvektor\n",b)
print("Koeffizientenmatrix\n",a)
x=gauss(a,b)
print("Lösung:x\n",x)