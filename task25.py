studentID=input("Enter your student ID: ")
studentAge=input("Enter your age: ")
workshopCode=input("Enter your workshop code: ")
paymentAmount=input("Enter the payment amount: ")
if studentID.isdecimal() and len(studentID) == 8:
    if studentAge.isascii() and studentAge.isdecimal() and 16 <= int(studentAge) <= 65:
        match workshopCode:
            case "PY":
                totalFee=30.0
            case "WEB":
                totalFee=40.0
            case "CY" if studentAge >= 18:
                totalFee=50.0
            case _:
                print("Invalid workshop code. Please enter a valid workshop code.")
        discount=0.2 if int(studentAge) <= 18 else 0
        finalFee=totalFee*(1-discount)
        if paymentAmount.isascii() and paymentAmount.isdecimal() and float(paymentAmount) >= finalFee:
            print("Registration confirmed.")
            print(studentID)
            print("PY" if workshopCode == "PY" else "WEB" if workshopCode == "WEB" else "CY")
            print(discount*100, "%")
            print("Final fee:", finalFee)
            print("Change:", totalFee-finalFee)
        else:
            print("Insufficient payment")
    else:
        print("Invalid age")
else:
    print("Invalid ID")