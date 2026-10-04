from time import time 

alter= int(input("Gib deinen Alter ein:"))
geburtsjahr = int(input("Gib deinen Geburtsjahr ein:"))

def pruefe_alter_geburtsjahr(alter,geburtsjahr):
    aktuelles_jahr = (int(time()/(365*24*60*60))) + 1970
    if aktuelles_jahr-geburtsjahr == alter:
        return True
    else: 
        return False

überprüfung = pruefe_alter_geburtsjahr(alter,geburtsjahr)
print(überprüfung)