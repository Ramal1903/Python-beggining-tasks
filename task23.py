assumeBalance=1000.0
storedPin="0427"
userPin=input("Enter your PIN: ")
amount=float(input("Enter the withdrawal amount: "))
if userPin.isascii()and userPin.isdecimal() and len(userPin) == 4 and amount%10==0 and amount <= assumeBalance:
    if userPin == storedPin:
        if amount < 200:
            fee=2.0
            amount = amount + fee
        else:
            fee=0
        assumeBalance = assumeBalance - amount
        print("Withdrawal amount:", amount)
        print("Fee:", fee)
        print("Your new balance:", assumeBalance)
    else:
        print("Incorrect PIN. Please try again.")
else:
    if not userPin.isascii():
        print("PIN should only contain ASCII characters. Please enter a valid PIN.")
    