firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))
if firstNumber > secondNumber and firstNumber > thirdNumber and secondNumber > thirdNumber:
    print(firstNumber, secondNumber, thirdNumber)
elif firstNumber > secondNumber and firstNumber > thirdNumber and thirdNumber > secondNumber:
    print(firstNumber, thirdNumber, secondNumber)
elif secondNumber > firstNumber and secondNumber > thirdNumber and firstNumber > thirdNumber:
    print(secondNumber, firstNumber, thirdNumber)
elif secondNumber > firstNumber and secondNumber > thirdNumber and thirdNumber > firstNumber:
    print(secondNumber, thirdNumber, firstNumber)
elif thirdNumber > firstNumber and thirdNumber > secondNumber and firstNumber > secondNumber:
    print(thirdNumber, firstNumber, secondNumber)
elif thirdNumber > firstNumber and thirdNumber > secondNumber and secondNumber > firstNumber:
    print(thirdNumber, secondNumber, firstNumber)