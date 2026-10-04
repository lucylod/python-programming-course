#es werden alle zahlen erzeugt, die sich als 7a+11b+13c darstellen lassen (bis 100)


M= {7*a + 11*b + 13*c for a in range(0,100) for b in range(0,100) for c in range(0,100)} 

#es wird geprüft ob die nächsten 13 zahlen in M sind
#n for n in M set-comprehension 
#erzeugt eine menge aller n aus M, die eine bestimmte bedingung erfüllen
#i läuft von 0 bis consecutive_max-1 (0 bis 12)
#wird überprüft, ob jede zahl n, n+1..., n+12 in menge enthalten ist
#all gibt true zurück wenn diese in der menge enthalten sind

consecutive_six={n for n in M if all((n+i) in M for i in range(13))}

n=(min(consecutive_six))

print(n-1)

