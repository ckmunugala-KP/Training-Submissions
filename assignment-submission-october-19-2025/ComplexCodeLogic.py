age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))

if age >= 18 and income >= 3000:
    print("Eligible for the program")
elif age >= 18 and income < 3000:
    print("Eligible but income too low")
else:
    print("Not eligible")
