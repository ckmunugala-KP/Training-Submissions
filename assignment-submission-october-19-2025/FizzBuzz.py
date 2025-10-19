num = int(input("Enter a number between 1 and 100: "))

if num < 1 or num > 100:
    print("Please enter a number within the range 1 to 100.")
else:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)