examScore=int(input("Enter your exam score: "))
if examScore < 0 or examScore > 100:
    print("Invalid exam score. Please enter a score between 0 and 100.")
else:
    result = "Pass" if examScore >= 51 else "Fail"
    print(result)