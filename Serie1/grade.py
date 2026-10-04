final_exam = 85
weekly_exam = 90
exercise = 65
total_grade = 0.4*final_exam + 0.4*weekly_exam + 0.2*exercise
print("Your final grade is",total_grade)



"""
        > 87,5% (sehr gut)
        > 75% (gut)
        > 62,5% (befriedigend)
        > 50% (genügend)
        <= 50% (nicht genügend)
"""

if total_grade  > 87.5:
    print ("Sehr gut")
elif total_grade > 75:
    print("Gut")
elif total_grade  > 62.5:
    print("Befriedigend")
elif total_grade > 50:
    print("Genügend")
else:
    print("Nicht Genügend")