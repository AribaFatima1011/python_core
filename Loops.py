#Table Generator
number = int(input("Enter a number:"))
print("Using For Loop")

for i in range(1,11):
    print(number, "*", i, "=", number * i)

print("Using While Loop")

i = 1
while i <= 10:
    print(number, "*", i, "=", number * i)
    i += 1

print("\nTable generated successfully!")