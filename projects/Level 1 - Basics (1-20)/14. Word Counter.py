def get_text(prompt="Enter Text: ") -> str:
    while True:
        text = input(prompt).strip()
        if text:
            return text
        else:
            print("Don't leave it empty")

def count_char(text) -> int: # all characters + whitespace 
    count = 0   # easy one line -> return len(text.replace(" ", ""))
    for char in text:
        count += 1

    return count


def count_char_no_whitespace(text) -> int:
    count = 0 # easy one line -> return len(text.replace(" ", ""))
    for word in text:
        for char in word:
            if char != " ":
                count += 1
    
    return count

def count_words(text) -> int:
    count = 0
    for word in text.split():
        count += 1
    
    return count

def main():
    while True:
        user_text = get_text()

        amount_char = count_char(user_text)
        amount_words = count_words(user_text)
        amount_char_no_whitespace = count_char_no_whitespace(user_text)

        print(f"\nTotal number of words: {amount_words}")
        print(f"Total number of characters (with space): {amount_char}")
        print(f"Total number of characters (without space): {amount_char_no_whitespace}")

        if input("\nAgain? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    main()