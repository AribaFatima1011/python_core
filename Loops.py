# Multiplication Table Generator

number = int(input("Enter a number: "))

print("\nUsing For Loop:")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


print("\nUsing While Loop:")

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

print("\nTable generated successfully!")