def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def is_palindrome(word):
    """Check if a string is a palindrome."""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def greet_user(name, greeting="Hello"):
    """Return a personalized greeting."""
    return f"{greeting}, {name}!"


# -----------------------------
# Main Program with User Input
# -----------------------------

def main():
    print("Welcome! Choose an operation:")
    print("1. Add two numbers")
    print("2. Multiply two numbers")
    print("3. Calculate average")
    print("4. Check palindrome")
    print("5. Greet user")
    print("6. Exit")

    while True:
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add_numbers(a, b))

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply_numbers(a, b))

        elif choice == "3":
            nums = input("Enter numbers separated by space: ")
            numbers = [float(n) for n in nums.split()]
            print("Average:", calculate_average(numbers))

        elif choice == "4":
            word = input("Enter a word: ")
            print("Palindrome?" , is_palindrome(word))

        elif choice == "5":
            name = input("Enter your name: ")
            print(greet_user(name))

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
