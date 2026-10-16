totalOrder=float(input("Enter the total order amount: "))
membershipStatus=input("Enter your membership status (yes/no): ")
if totalOrder < 0 or (membershipStatus != "yes" and membershipStatus != "no"):
    print("Invalid order amount or membership status. Please enter a positive value for the order amount and 'yes' or 'no' for membership status.")
else:
    deliveryFee = 0 if totalOrder >= 50 or membershipStatus == "yes" else 5.0
    print(totalOrder + deliveryFee)
    