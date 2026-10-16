drinkCode=input("Enter the drink code (C for Coffee, T for Tea, J for Juice): ")
quantity=int(input("Enter the quantity: "))
tea=2.0
coffee=4.0
juice=3.0
match drinkCode:
    case "C" if quantity > 0:
        orderAmount = coffee * quantity
        print(orderAmount)
    case "T" if quantity > 0:
        orderAmount = tea * quantity
        print(orderAmount)
    case "J" if quantity > 0:
        orderAmount = juice * quantity
        print(orderAmount)
    case _:
        print("Invalid drink code or quantity.")
result = "Large order" if quantity >= 20 else "Regular order"
print(result)