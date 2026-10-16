userAge=int(input("Enter your age: "))
monthlySalary=int(input("Enter your monthly salary: "))
requestedLoanAmount=int(input("Enter the requested loan amount: "))
if userAge <=0 or monthlySalary <=0 or requestedLoanAmount <=0:
    print("Invalid input. Please enter positive values.")
else:
    if userAge < 18 or monthlySalary < 500 or requestedLoanAmount > 10 * monthlySalary:
        print("Loan request denied.")
    else:
        print("Loan request approved.")
        
        