letters = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6, "G":7,"H":8,"I":9,"J":10,
           "K":11,"L":12, "M":13, "N":14, "O":15, "P":16,"Q":17,"R":18,
           "S":19,"T":20,"U":21, "V":22, "W":23,"X":24,"Y":25,"Z":26}

# k = Buchstabe, v = Zahl
# Erstellt umgekehrtes Dictionary: Zahl -> Buchstabe
numbers = {v: k for k, v in letters.items()}

def encrypt(m): 
    m = m.upper()                   
    verschluesselt = ""             

    for buchstabe in m:             
        if buchstabe in letters:    
            zahl = letters[buchstabe]  #buchstabe -> zahl     
            neue_zahl = zahl + 1    
            if neue_zahl > 26:      
                neue_zahl = 1
            verschluesselt += numbers[neue_zahl]  #wandelt zahl zurück in einem buchstaben
        else:
            verschluesselt += buchstabe 

    return verschluesselt            

def decrypt(m):
    m = m.upper()                     
    entschluesselt = ""               

    for buchstabe in m:               
        if buchstabe in letters:      
            zahl = letters[buchstabe]       
            neue_zahl = zahl - 1      
            if neue_zahl < 1:         
                neue_zahl = 26
            entschluesselt += numbers[neue_zahl]  
        else:
            entschluesselt += buchstabe  

    return entschluesselt            

print(encrypt("ABC"))   
print(encrypt("XYZ"))   
print(decrypt("BCD"))   
print(decrypt("YZA"))   
