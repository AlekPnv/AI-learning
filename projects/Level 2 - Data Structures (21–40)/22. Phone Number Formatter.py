def num_formatter():
    while True:
        phone_num = input("10 digit - Number: ")
        
        if phone_num.startswith("+"):
            # can't figure out anything else on how to seperate the (+xx) because it can be 1-3 digits
            digits = "".join(filter(str.isdigit, phone_num))
            print(digits)
            if len(digits) < 10:
                print("Invalid phone number\n")
                continue
            
            formatted_num = f"+{digits[:(len(digits)-10)]} " + f"({digits[(len(digits)-10):(len(digits)-7)]}) " + digits[(len(digits)-7):(len(digits)-4)] + "-" + digits[(len(digits)-4):]
            print(formatted_num)
            
        else:
            digits = "".join(filter(str.isdigit, phone_num))
            
            if len(digits) != 10:
                print("Invalid phone number\n")
                continue
            
            formatted_num = f"({digits[:3]}) " + digits[3:6] + "-" + digits[6:] 
            print(formatted_num)
        
        if input("\n Again? [y/n]: ").strip().lower() != "y":
            break

if __name__ == "__main__":
    num_formatter()


""" IMPROVED VERSION
def num_formatter():
    while True:
        phone_num = input("Enter phone number: ").strip()

        digits = "".join(filter(str.isdigit, phone_num))

        # Validation
        if len(digits) < 10 or len(digits) > 13:
            print("Invalid phone number\n")
            continue

        # Without country code
        if len(digits) == 10:
            formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        
        # With country code
        else:
            country_code = digits[:-10]
            local = digits[-10:]
            formatted = f"+{country_code} ({local[:3]}) {local[3:6]}-{local[6:]}"
        
        print(f"Formatted: {formatted}")

        if input("\nAgain? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    num_formatter()
"""