def ableitung(stammfunktion):
    dx = [stammfunktion[1]]


    #koeffizienten an position wird werden mit seinem exponenten multiplziert und an der liste angehängt
    #es wird durch alle indizes von 2 bis zum ende der liste stammfunkton durchlaufen 
    [dx.append(stammfunktion[i]*i) for i in range (2,len(stammfunktion))]

    return dx

my_list=[1,2,3,4,5,6,7,8,9,10]

dx=ableitung(my_list)

print(dx)


