class InvalidScoreError(Exception):
    """Custom exception raised when score is not between 0 and 100."""
    pass

def calculate_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number.")
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    user_input = input("Enter your score: ")
    score_value = float(user_input)  # may raise ValueError
    grade = calculate_grade(score_value)

except ValueError:
    print("Error: Please enter a valid numeric value.")
except TypeError as e:
    print(f"Type Error: {e}")
except InvalidScoreError as e:
    print(f"Custom Error: {e}")
else:
    print(f"Grade calculated successfully! Your grade is: {grade}")
finally:
    print("Program finished — exception handling demo complete.")
