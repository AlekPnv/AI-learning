# Imported Libaries
from pwinput import pwinput

# Constant Variables
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"


# Password Checker Function
def password_checker():
    # Initialize repeating loop
    while True:
        # Set Values
        n_lowercase = 0
        n_uppercase = 0
        n_numbers = 0
        n_symbols = 0
        n_requirements = 0
        strength_score = 0
        consec_lower = 0
        consec_upper = 0
        consec_num = 0
        result = ""
        reasons = ""


        # User-Password-Input
        password = pwinput("Enter password: ")
        password_lenght = len(password)



        # Check what characters are given 
        for char in password: 
            if char in LOWERCASE_LETTERS:
                n_lowercase += 1
            elif char in UPPERCASE_LETTERS:
                n_uppercase += 1
            elif char in NUMBERS:
                n_numbers += 1
            elif char in SYMBOLS:
                n_symbols += 1
            else:
                print("There appears to be an unidentifiable character")

        # Measuring the Strenght (simplified)
        # Additions (Almost all)
        add_score = 0

        n_middle_num = round((password_lenght-2)/2)

        if password_lenght >= 16:
            n_requirements += 1
            reasons += "+ Password is atleast 16 characters long\n"
        if n_lowercase >= 1:
            n_requirements += 1
            reasons += "+ Password contains atleast 1 lower case letter\n"
        if n_uppercase >= 1:
            n_requirements += 1
            reasons += "+ Password contains atleast 1 upper case letter\n"
        if n_numbers >= 1:
            n_requirements += 1
            reasons += "+ Password contains atleast 1 number\n"
        if n_symbols >= 1:
            n_requirements += 1
            reasons += "+ Password contains atleast 1 special character\n"

        add_score = password_lenght*4 + ((password_lenght-n_lowercase)*2) + ((password_lenght-n_uppercase)*2) + n_numbers*4 + n_symbols*6 + n_middle_num*2 + n_requirements*2

        # Deductions (Not all)
        ded_score = 0
        for i in range(1, password_lenght):
            if password[i].islower() and password[i-1].islower():
                consec_lower += 1
            elif password[i].isupper() and password[i-1].isupper():
                consec_upper += 1
            elif password[i].isdigit() and password[i-1].isdigit():
                consec_num += 1

        if consec_lower >= 1:
            reasons += "- The password contains consecutive lowercase letters\n"
        if consec_upper >= 1:
            reasons += "- The password contains consecutive uppercase letters\n"
        if consec_num >= 1:
            reasons += "- The password contains consecutive numbers\n"

        if n_lowercase == password_lenght or n_uppercase == password_lenght or n_numbers == password_lenght:
            ded_score += password_lenght
            reasons += "- The password contains only lowercase, uppercase or numbers\n"

        ded_score += consec_lower*2 + consec_upper*2 + consec_num*2

        # Final Score / Strenght / Time-to-Crack
        strength_score = add_score - ded_score

        # Set minimum and maximum
        if strength_score < 0:
            strength_score = 0
        elif strength_score > 100:
            strength_score = 100

        # Get the last result text based on the score
        if strength_score <= 20:
            result = "Very Weak"
        elif strength_score <= 40:
            result = "Weak"
        elif strength_score <= 60:
            result = "Medium"
        elif strength_score <= 80:
            result = "Strong"
        elif strength_score <= 100:
            result = "Very Strong"


        print(f"Overall Strength: {strength_score} out of 100 - {result}\n")
        print(f"Reasons:\n{reasons}")

        repeat = input("Check Another? [y/n]: ").lower()
        if repeat != "y":
            break

if __name__ == "__main__":
    password_checker()

"""Corrected Version:
# Character sets
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"


def password_checker():
    while True:
        password = input("Enter password: ")

        if not password:
            print("Password cannot be empty.\n")
            continue

        length = len(password)
        lower = upper = digits = symbols = 0
        consec_lower = consec_upper = consec_digit = 0
        reasons = []

        # Count characters
        for i, ch in enumerate(password):
            if ch in LOWER:
                lower += 1
                if i > 0 and password[i-1] in LOWER:
                    consec_lower += 1
            elif ch in UPPER:
                upper += 1
                if i > 0 and password[i-1] in UPPER:
                    consec_upper += 1
            elif ch in DIGITS:
                digits += 1
                if i > 0 and password[i-1] in DIGITS:
                    consec_digit += 1
            elif ch in SYMBOLS:
                symbols += 1

        # Scoring
        score = length * 4
        score += (length - lower) * 2
        score += (length - upper) * 2
        score += digits * 4
        score += symbols * 6

        score -= (consec_lower + consec_upper + consec_digit) * 2

        if lower == length or upper == length or digits == length:
            score -= length
            reasons.append("- Only one character type used")

        # Feedback
        if length < 8:
            reasons.append("- Too short")
        if lower == 0:
            reasons.append("- No lowercase letters")
        if upper == 0:
            reasons.append("- No uppercase letters")
        if digits == 0:
            reasons.append("- No numbers")
        if symbols == 0:
            reasons.append("- No symbols")

        score = max(0, min(score, 100))

        if score <= 20:
            strength = "Very Weak"
        elif score <= 40:
            strength = "Weak"
        elif score <= 60:
            strength = "Moderate"
        elif score <= 80:
            strength = "Strong"
        else:
            strength = "Very Strong"

        print(f"\nStrength: {score}/100 — {strength}")
        if reasons:
            print("Issues:")
            for r in reasons:
                print(r)

        if input("\nCheck another? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    password_checker()
"""