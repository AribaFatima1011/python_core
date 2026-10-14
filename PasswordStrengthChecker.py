password = input("Enter Password:")
upper = False
lower = False
digit = False

for x in password:
    if x.isupper():
        upper = True
    if x.islower():
        lower = True
    if x.isdigit():
        digit = True

if len(password) >= 8 and upper and lower and digit:
    print("Strong Password")
elif len(password) < 6:
    print("Weak Password")
else:
    print("Moderate Password")
         