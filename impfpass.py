import time

class Impfpass:

    def __init__(self):
        
        
        #wichtig: _ ist eine konvention und bedeutet: protected attribut.
        #d.h sie darf innerhalb der klasse verwendet werden, darf aber von außen nicht direkt geändert werden

        self._geimpft=False
        self._genesen=False


        self._getestet=time.time()-25*3600


    def _set_geimpft(self):
        self._geimpft=True
    
    def _set_genesen(self):
        self.genesen=True


    def _set_getestet(self):

        self._getestet=time.time()

    
    def einlass_erlaubt(self):
        #Fall 1
        if self._geimpft or self._set_genesen:
            return True
        

        #Fall 2

        aktuelle_zeit=time.time()

        return (aktuelle_zeit-self._getestet)<=24*3600
    

impfpass=Impfpass()

print(f"Einlass erlaubt:{impfpass.einlass_erlaubt()}.")

impfpass._set_getestet()
print(f"Einlass erlaubt:{impfpass.einlass_erlaubt()}.")

