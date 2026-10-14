def tipCalculate(bill, tip_percent):
    totalTip = bill * tip_percent / 100
    return totalTip

def billCalculate(bill, tip_val):
    totalBill = originalBill + tip_val
    return totalBill

def billPerPerson(billAmount, noOfPersons):
    return(billAmount / noOfPersons)

originalBill = float(input("Enter Total Resturant Bill Amount:"))
tipPercent = int(input("Enter Percentage Tip:"))
numOfPersons = int(input("Enter number of persons:"))

tip = tipCalculate(originalBill, tipPercent)

bill = billCalculate(originalBill, tip)
print(f"Your total bill is {bill}")

bill_per_person = billPerPerson(bill, numOfPersons)
print(f"Total bill per person is {bill_per_person}")

