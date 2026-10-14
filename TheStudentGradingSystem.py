students = {
    "Ariba" : 100,
    "Fatima" : 95,
    "Sarim" : 80,
    "Wahab" : 85,
    "Zara" : 69
}
for name,marks in students.items():
    if(marks >= 90):
        print("Grade:A+")
    elif(marks >= 80):
        print("Grade:B")
    elif(marks >= 70):
        print("Grade:C")
    else:
        print("Fail")