import string

def main():
    while True:
        text = input("Enter Text: ").strip()
        
        if not text:
            print("Input cannot be empty.")
            continue
        
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        
        if not words:
            print("Input must contain valid words.")
            continue
        
        word_dict = counter(words)

        print("\nWord Frequencies:")
        for word in sorted(word_dict):
            print(f"{word} -> {word_dict[word]}")

        most_frequent = max(word_dict, key=word_dict.get) # type: ignore

        print(f"\nMost frequent word: {most_frequent}")
        print(f"Total words: {len(words)}")
        print(f"Unique words: {len(word_dict)}")

        if input("\nAgain? [y/n]: ").lower() != "y":
            break


def counter(text):
    word_dict = {}
    for word in text:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


if __name__ == "__main__":
    main()