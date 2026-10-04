import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


data = np.loadtxt("federkennlinie.csv",delimiter=",")


x=data[:,0]
F=data[:,1]


a,b=sp.symbols("a b", positive=True)
xi=sp.Symbol("xi", real=True)

f_sym=(xi/a)*sp.Abs(sp.tanh(xi/b))

S=0

for xk,Fk in zip(x,F):
    S+=(f_sym.subs(xi,xk)-Fk)**2

eq1 = sp.diff(S,a)
eq2 = sp.diff(S,b)

a0=1.0
b0=1.0

sol=sp.nsolve([eq1,eq2],[a,b],[a0,b0])

a_opt=float(sol[0])
b_opt=float(sol[1])

def model_np(x,a,b):
    return(x/a)*np.abs(np.tanh(x/b))

x:fine=np.linspace(x.min(),x.max())
plt.plot(x,F, "gx", label="Messdaten")
plt.plot(x_fine, model_np(x_fine, a_opt, b_opt),"-",label="Fit")
plt.legend(loc="lower right")


t.text(0.05, 0.95, f"a = {a_opt:.1f}\nb = {b_opt:.1f}",
         transform=plt.gca().transAxes, va="top",
         bbox=dict(boxstyle="round", facecolor="white"))



plt.show()

with open("parameter.txt", "w") as f:
    f.write(f"a={a_opt}\n")
    f.write(f"b={b_opt}\n")
            