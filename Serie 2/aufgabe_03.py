import math
pi = math.pi 
approx1 = 3
rel_error1 = abs(pi-approx1)/pi 
percent_error1= rel_error1*100
print("Pi kann durch",approx1,"mit einem relativen Fehler von {:.4f}".format(rel_error1),"approximiert werden. Das sind {:.2f}% Fehler.".format(percent_error1))


approx2 = 3.14
rel_error2 = abs(pi-approx2)/pi
percent_error2 = rel_error2*100
print("Pi kann durch", approx2, "mit einem relativen Fehler von {:.4f} approximiert werden. Das sind {:.2f}% Fehler.".format(rel_error2, percent_error2))

approx3 = 22/7 
rel_error3= abs(pi-approx3)/pi
percent_error3 = rel_error3*100
print("Pi kann durch", approx3, "mit einem relativen Fehler von {:.4f} approximiert werden. Das sind {:.2f}% Fehler.".format(rel_error3, percent_error3))

approx4 = 355/113
rel_error4 = abs(pi-approx4)/pi
percent_error4= rel_error4*100
print("Pi kann durch", approx4, "mit einem relativen Fehler von {:.7f} approximiert werden. Das sind {:.5f}% Fehler.)".format(rel_error4, percent_error4))