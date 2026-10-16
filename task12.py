travelDistance = float(input("Enter the travel distance in kilometers: "))
if travelDistance <= 0:
    print("Invalid distance")
else:
    startingFee = 2.0
    if travelDistance <= 5:
        totalFee = startingFee + (travelDistance * 0.7)
    elif travelDistance <= 15:
        totalFee = startingFee + (5 * 0.7) + ((travelDistance - 5) * 0.6)
    else:
        totalFee = startingFee + (5 * 0.7) + (10 * 0.6) + ((travelDistance - 15) * 0.5)
    print("Total travel fee:", totalFee, "AZN")