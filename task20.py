studentID=input("Enter your student ID: ")
if studentID.isdecimal() and len(studentID) == 8:
    print("Student ID accepted.")
elif not studentID.isdecimal():
    print("Your student ID should only contain numbers. Please enter a valid student ID.")
elif len(studentID) != 8:
    print("Your student ID should be 8 digits long. Please enter a valid student ID.")