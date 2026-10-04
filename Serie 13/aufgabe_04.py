import sympy as sp

x, a, b = sp.symbols('x a b', real=True)
c0, c1, c2, c3 = sp.symbols('c0 c1 c2 c3', real=True)

p = c0 + c1*x + c2*x**2 + c3*x**3

eqs = []
for k in range(4):  # k=0..3
    eqs.append(sp.Eq(sp.integrate(p * x**k, (x, a, b)), b**k))

sol = sp.solve(eqs, [c0, c1, c2, c3], dict=True)[0]
p_sol = sp.simplify(p.subs(sol))

print("p(x) =", p_sol)
