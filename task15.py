examScore=int(input("Enter your exam score: "))
schoolScore=int(input("Enter your school score: "))
userAge=int(input("Enter your age: "))
if userAge < 16 or examScore < 0 or examScore > 700 or schoolScore < 0 or schoolScore > 100:
    print("Invalid input. Please enter valid values.")
else:
    if examScore >= 600:
        print("You are eligible for Scholarship.")
    elif examScore >= 450:
        print("You are eligible for Admission.")
    elif 300 <= examScore < 450 and schoolScore >= 80:
        print("You are eligible for Admission.")
    else:
        print("You are not eligible for Scholarship or Admission.")
    