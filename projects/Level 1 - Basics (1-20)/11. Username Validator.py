def username_validator():
    LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SYMBOLS = "!@#$%^&*()-=+[]{}|;:'\",.<>?/`~" # remove the _ underscore
    
    while True:
        print("------------------------")
        username = input("Enter username: ")
        invalid = []
        
        if len(username) == 0:
            invalid.append("- Username can't be empty")

        if len(username) > 15:
            invalid.append("- Username is too long")
        
        if len(username) < 5:
            if username:
                invalid.append("- Username is too short")

        if " " in username:
            invalid.append("- Username can't contain spaces")

        if username and username[0] not in LETTERS: # Alternative -> if username and not username[0].isalpha():
            invalid.append("- Username can only start with a letter")

        if any(ch in SYMBOLS for ch in username): # Alternative -> if not all(ch.isalnum() or ch == "_" for ch in username):
            invalid.append("- Username can only contain letters, numbers and underscores")

        if invalid:
            print("\nInvalid username:")
            for msg in invalid:
                print(msg)
        else:
            print("Valid username")
        
        if input("\nAgain? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    username_validator()