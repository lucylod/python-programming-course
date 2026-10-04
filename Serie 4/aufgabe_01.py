def matrix_kennwerte(A):

    z1=abs(A[0][0])+ abs(A[0][1])+ abs(A[0][2])
    z2=abs(A[1][0])+abs(A[1][1])+abs(A[1][2])
    z3=abs(A[2][0])+abs(A[2][1])+abs(A[2][2])
    s1=abs(A[0][0])+abs(A[1][0])+abs(A[2][0])
    s2=abs(A[0][1])+abs(A[1][1])+abs(A[2][1])
    s3=abs(A[0][2])+abs(A[1][2])+abs(A[2][2])
    spur= A[0][0]+A[1][1]+A[2][2]

    return z1,z2,z3,s1,s2,s3,spur


werte=list(map(int,input("Gib 9 Zahlen für die 3x3-Matrix ein:").split()))
A=[werte[:3],werte[3:6],werte[6:9]]


z1,z2,z3,s1,s2,s3,spur=matrix_kennwerte(A)
zeilensummenform=max(z1,z2,z3)
spaltensummenform=max(s1,s2,s3)

print(f"Matrix:{A}")
print(f"Zeilensummen: {z1},{z2},{z3}")
print(f"Zeilensummenform:{zeilensummenform}")
print(f"Spaltensummen: {s1},{s2},{s3}")
print(f"Spaltensummenform: {spaltensummenform}")
print(f"Spur:{spur}")
