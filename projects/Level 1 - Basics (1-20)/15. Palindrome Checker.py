def get_text(prompt="Enter text: ") -> str:
    table = {ord("!"):"",
            ord("?"):"",
            ord("."):"",
            ord(" "):"",
            ord(","):"",
            ord("/"):"",
            ord("-"):"",
            ord("_"):""
        }
    
    while True:
        text = input(prompt).lower().translate(table) # replace all the table stuff in ASCII with ""
        if text:
            return text
        else:
            print("Don't leave it empty\n")
            continue


def palindrome_checker(text) -> bool:
    for i in range(len(text) // 2):
        if text[i] != text[-i-1]:
            return False
    return True


def main():
    while True:
        user_input = get_text()
        
        print(f"\nResult {'is' if palindrome_checker(user_input) else 'is not'} a palindrome")

        if input("\nAgain? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    main()