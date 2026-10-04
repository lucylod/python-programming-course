def person_dict():

    my_dict={
        "Vorname":input("Gib deinen Vornamen an"), 
        "Nachname":input("Gib deinen Nachnamen an"),
        "Alter":int(input("Gib deinen Alter an"))
    }
    if my_dict["Alter"]>=18:
        return my_dict
    else:
        print("Ungültige Eingabe")
        return None

my_dict=person_dict()

if my_dict:
    liste=list(my_dict.values())
    print(my_dict)
    print(liste)

