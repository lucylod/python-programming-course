import math
N = int(input("Die Anzahl der Personen in einer Gruppe"))
P = 1- (math.factorial(365)/(365**N*math.factorial(365-N)))
P_percent = P*100
print("Die Wahrscheinlichkeit, dass in einer Gruppe mind. zwei Personen am selben Tag Geburtstag haben, beträgt {:.2f}%".format(P_percent))


#Bonus

for N_needed in range(1,101):
    P_check = 1 - (math.factorial(365)/(365**N_needed*math.factorial(365-N_needed)))
    if P_check > 0.5:
        print("Bei einer Anzahl von", N_needed, "Personen beträgt die Wahrscheinlichkeit größer als 50%." )
        break 


    