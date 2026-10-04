a = int(input("Enter the number: "))

while a != 60:
    if a < 60:
        print("The number is very low")
    else:
        print("The number is very high")

    a = int(input("Try again: "))

print("The number is correct")
