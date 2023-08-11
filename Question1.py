    number = float(input("Enter a number: "))
        if 0 <= number <= 10:
            print("Low Range")
        elif 11 <= number <= 50:
            print("Medium Range")
        elif 51 <= number <= 100:
            print("High Range")
        else:
            print("Out of Range")
