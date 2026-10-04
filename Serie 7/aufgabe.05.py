def diff(f,x,h_0,eps):

    def phi(h):
       return (f(x+h)-f(x))/h

    
    h=h_0
    phi_alt=phi(h)
    n=0

    while True:
        h=h/2
        phi_neu=phi(h)
        fehler=abs(phi_alt-phi_neu)

        if fehler <= eps*abs(phi_alt):
            break

        phi_alt=phi_neu
        n +=1

    return phi_neu,h,n
    

        






