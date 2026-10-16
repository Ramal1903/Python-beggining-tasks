examScore=int(input("Enter your exam score: "))
if 100 >= examScore >= 91:
    print("Your grade is A.")
elif 90 >= examScore >= 81:
    print("Your grade is B.")
elif 80 >= examScore >= 71:
    print("Your grade is C.")
elif 70 >= examScore >= 61:
    print("Your grade is D.")
elif 60 >= examScore >= 51:
    print("Your grade is E.")
elif 50 >= examScore >= 0:
    print("Your grade is F.")
else:
    print("Invalid score.")