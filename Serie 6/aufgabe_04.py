
#was ist map()? führt eine funktion auf jedes element einer liste aus

def mymap(funktion,iterable):
    my_list=[]

    for element in iterable:
        my_list.append(funktion(element))
    
    return my_list


#problem: gibt immer eine liste zurück, keinen iterator wie bei map().

print(mymap(lambda x: x*2,[1,2,3]))
print("Wir haben eine Liste von Temperaturen in Fahrenheit:",mymap(lambda temp:(temp*9/5)+32, [0.0,10.0,20.0,30.0,40.0,50.0]))
print(mymap(lambda x: x*2,(1,2,3)))

def my_map(funktion,iterable):
    for element in iterable:
        yield funktion(element) #oder stattdassen klassen (noch nicht gelernt)

print(list(my_map(lambda x: x*2,[1,2,3])))
print(list(my_map(lambda x: x*x,[1,2,3])))
print(tuple(my_map(lambda x: x*x,[1,2,3])))
print(set(my_map(lambda x: x*x,[1,2,3])))


#was macht filter()? #behält nur die elemente, die eine bedingung erfüllen

def myfilter(funktion, iterable):
    return (x for x in iterable if funktion(x))

grades=[91,32,83,44,75,56,67]
print("Wir haben eine liste von bestandenen Noten:",list(myfilter(lambda grade: grade >= 60, grades)))

def myreduce(funktion,iterable):
    ergebnis=iterable[0]

    for element in iterable[1:]:
        ergebnis=funktion(ergebnis,element)

    return ergebnis

print(myreduce(lambda a,b:a+b,[1,2,3]))




