import numpy as np

A=np.array([
    [1,1,2],
    [2,3,1],
    [7,9,-3]
],dtype=float)

b=np.array([3,5,0],dtype=float)
x1=np.linalg.solve(A,b)
print("Lösung mit np.linalg.solve:",x1)

A_inv=np.linalg.inv(A)
x2=np.dot(A_inv,b)
print("Lösung über die Inverse",x2)


Probe=np.dot(A,x2)
print("Probe",Probe)













