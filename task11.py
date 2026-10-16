
usage = float(input("Enter monthly electricity usage (kWh): "))

if usage < 0:
    print("Invalid usage")
else:
    if usage <= 100:
        rate = 0.08
    elif usage <= 300:
        rate = 0.12
    else:
        rate = 0.15
    bill = usage * rate
    print("Usage:", usage, "kWh")
    print("Applied rate:", rate, "AZN/kWh")
    print("Total bill:", bill, "AZN")
