productCode=input("Enter your product code: ")
quantity=int(input("Enter the quantity (1-5): "))
couponCode=input("Enter the coupon code: ")
deliveryCode=input("Enter the delivery code: ")
keyboard=40.0
mouse=20.0
headphone=60.0
match productCode:
    case "K" if 5 >= quantity > 0:
        subTotal = keyboard * quantity
    case "M" if 5 >= quantity > 0:
        subTotal = mouse * quantity
    case "H" if 5 >= quantity > 0:
        subTotal = headphone * quantity
    case _:
        print("Invalid product code or quantity.")
discount = 0
finalTotal = subTotal
if couponCode == "SAVE10" and subTotal >= 100:
    discount = finalTotal * 0.10
    finalTotal = finalTotal - discount
elif couponCode != "SAVE10" or couponCode != "NONE":
    print("Invalid coupon code.")
match deliveryCode:
    case "P":
        deliveryFee = 0
    case "S":
        deliveryFee = 0 if subTotal >= 80 else 5.0
        finalTotal = finalTotal + deliveryFee
    case _:
        print("Invalid delivery code.")
match productCode:
    case "K":
        print("Product: Keyboard")
        print("Quantity:", quantity)
        print("Subtotal: ", subTotal , "AZN")
        print("Discount: ", discount , "AZN")
        print("Delivery Fee: ", deliveryFee , "AZN")
        print("Final Total: ", finalTotal , "AZN")
    case "M":
        print("Product: Mouse")
        print("Quantity:", quantity)
        print("Subtotal: ", subTotal , "AZN")
        print("Discount: ", discount , "AZN")
        print("Delivery Fee: ", deliveryFee , "AZN")
        print("Final Total: ", finalTotal , "AZN")
    case "H":
        print("Product: Headphone")
        print("Quantity:", quantity)
        print("Subtotal: ", subTotal , "AZN")
        print("Discount: ", discount , "AZN")
        print("Delivery Fee: ", deliveryFee , "AZN")
        print("Final Total: ", finalTotal , "AZN")
