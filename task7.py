userAge=int(input("Enter your age: "))
if 12>=userAge>=0:
    print("You are a child.")
elif 17>=userAge>=13:
    print("You are a teenager.")
elif 64>=userAge>=18:
    print("You are an adult.")
elif userAge>=65:
    print("You are a senior.")
else:
    print("Invalid age.")