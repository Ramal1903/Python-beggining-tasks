stored_pin = "0427"
userPin = input("Enter your PIN: ")
if userPin:
    if len(userPin) == 4:
        if userPin.isdecimal() and userPin.isascii():
            if userPin == stored_pin:
               print("Access granted")
            else:
               print("Incorrect PIN")
        else:
           print("Digits only")
    else:
        print("PIN must have 4 digits")
else:
    print("PIN is required")