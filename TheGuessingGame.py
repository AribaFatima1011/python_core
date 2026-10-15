secretNumber = 42
attempt = 0
while attempt < 5:
    number = int(input("Guess the number:"))
    if number < 1 or number >100:
        print("Invalid Number(Range 1-100).")
        continue
    elif number == secretNumber:
        print("Congratulations!You got it")
        break
    elif number != secretNumber:
        attempt += 1
else:
    print("Game Over! You lost.")
         