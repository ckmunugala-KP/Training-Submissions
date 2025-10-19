print("Choose a pattern to print:")
print("1. Right-Angle Triangle")
print("2. Pyramid")

choice = input("Enter your choice (1 or 2): ")

rows = int(input("Enter the number of rows: "))

if choice == "1":
    print("\nRight-Angle Triangle Pattern:\n")
    for i in range(1, rows + 1):
        print("*" * i)

elif choice == "2":
    print("\nPyramid Pattern:\n")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

else:
    print("Invalid choice. Please enter 1 or 2.")