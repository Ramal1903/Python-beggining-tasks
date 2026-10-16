
balance = 1000

amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Remaining balance:", balance, "AZN")
