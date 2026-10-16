
firstlength = int(input("Enter the first side of the triangle: "))
secondlength = int(input("Enter the second side of the triangle: "))
thirdlength = int(input("Enter the third side of the triangle: "))

if firstlength + secondlength > thirdlength:
    if firstlength + thirdlength > secondlength:
        if secondlength + thirdlength > firstlength:
            if firstlength == secondlength:
                if secondlength == thirdlength:
                     print("The triangle is equilateral.")
                else:
                    print("The triangle is isosceles.")
            else:
                if firstlength == thirdlength:
                    print("The triangle is isosceles.")
                else:
                    if secondlength == thirdlength:
                            print("The triangle is isosceles.")
                    else:
                        print("The triangle is scalene.")
        else:
            print("Triangle cannot be created.")
    else:
        print("Triangle cannot be created.")
else:
    print("Triangle cannot be created.")
        