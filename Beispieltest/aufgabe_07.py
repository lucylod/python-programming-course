import numpy as np

def compute_house_values(n):


    if n < 1:
        raise ValueError
    
    if n == 1:
        return np.array([0.0, 0.0])

    m=n-1

    A=2*np.eye(m)

    A +=-1*np.eye(m,k=1)
    A+=-1*np.eye(m,k=1)
    b=20000*np.ones(m)

    x_inner=np.linalg.solve(A,b)
    x=np.zeros(n+1)
    x[1:n]=x_inner

    return x


print(compute_house_values(4))

