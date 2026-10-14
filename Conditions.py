print("Student Result Card")
number = float(input('Enter marks of student:'))
if number >= 90:
    print("A+")
elif number >= 80 and number < 90:
    print("A")
elif number >= 70 and number < 80:
    print("B+")
elif number >= 60 and number < 70:
    print("C+")
elif number >= 50 and number < 60:
    print("D+")
else:
    print("Fail")
