
amount = float(input("Enter purchase amount: "))
if amount < 100:
    discount = 0
elif amount < 300:
    discount = 10
elif amount < 500:
    discount = 15
else:
    discount = 20
discount_amount = amount * discount / 100
final_price = amount - discount_amount
print("Original Price:", amount, "AZN")
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount, "AZN")
print("Final Price:", final_price, "AZN")
