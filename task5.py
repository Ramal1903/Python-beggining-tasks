firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))
if firstNumber > secondNumber and firstNumber > thirdNumber:
    print("The first number is the greatest.")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print("The second number is the greatest.")
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print("The third number is the greatest.")
else:
    print("There is a tie for the greatest number.")