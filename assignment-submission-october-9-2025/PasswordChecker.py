import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Moderate"
    if not re.search(r"[a-z]", password):
        return "Moderate"
    if not re.search(r"\d", password):
        return "Moderate"
    if not re.search(r"[!@#$%^&*()_+=\-]", password):
        return "Moderate"
    return "Strong"

try:
    pwd = input("Enter your password: ").strip()
    if not pwd:
        raise ValueError("Password cannot be empty.")
    print("Password Strength:", check_password_strength(pwd))
except Exception as e:
    print("Error:", e)
