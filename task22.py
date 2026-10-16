phoneNumber = input("Enter your phone number: ")
if phoneNumber.isdecimal() and len(phoneNumber) == 10:
    match phoneNumber[:3]:
        case "050" | "051" | "055" | "070" | "077" | "099":
            print("Phone number accepted")
        case _:
            print("Invalid phone number. Please enter a valid phone number.")
else:
    print("Invalid phone number. Please enter a valid phone number.")