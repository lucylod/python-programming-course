def newton(f,fprime,x0,tol):
    x=x0

    while True:

        if abs(fprime(x))<=tol*abs(f(x)):
            raise ValueError("Newton-Abbruch: Ableitung zu klein.")     
        
        x_former=x
        x_new=x-(f(x)/fprime(x))
        x=x_new
        
        if abs(f(x))<tol or abs((x-x_former))<tol:
            return x
        
result = newton(lambda x: x**2-2,
                lambda x:2*x,
                1,
                1e-6)

print(result)
        


