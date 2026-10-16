firstNumber=int(input("Enter first number: "))
secondNumber=int(input("Enter second number: "))
operation=input("Enter operation")
if operation == "+":
    result = firstNumber + secondNumber
    print("The result is:", result)
elif operation == "-":
    result = firstNumber - secondNumber
    print("The result is:", result)
elif operation == "*":
    result = firstNumber * secondNumber
    print("The result is:", result)
elif operation == "/":
    if secondNumber != 0:
        result = firstNumber / secondNumber
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "%":
    if secondNumber != 0:
        result = firstNumber % secondNumber
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "**":
    if firstNumber == 0 and secondNumber < 0:
        print("Error: Zero cannot be raised to a negative power.")
    else:
        result = firstNumber ** secondNumber
        print("The result is:", result)
elif operation == "//":
    if secondNumber != 0:
        result = firstNumber // secondNumber
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")