bank_balance = 5000
def deposit(amount):
    global bank_balance
    bank_balance += amount 
def withdraw(amount):
    global bank_balance
    if bank_balance >= amount:
        bank_balance -= amount
    else:
        print("Don't exceed from your current balance")
deposit(1000)
print(f"Current Balance after deposit is {bank_balance}")
withdraw(2000)
print(f"Current Balance after withdraw is {bank_balance}")