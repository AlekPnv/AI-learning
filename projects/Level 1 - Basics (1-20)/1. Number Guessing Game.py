import random


def number_guessing_game():
    print("Welcome to the Guessing Game!\n")
    
    while True:
        tries = 0
        
        try:
            difficulty = int(input("Choose a difficulty: Easy[1] or Hard[2]\n"))
        except (ValueError, FloatingPointError):
            print("Try again with a whole number between 1 and 2")
            
        if difficulty == 1:
            max_num = 50
        elif difficulty == 2:
            max_num = 100
        else:
            print("Invalid Difficulty. \n")
        
        target_num = random.randint(1,max_num)
        while True:
            try:
                user_guess = int(input(f"Guess a number between 1 and {max_num}: "))
            except ValueError:
                print("Enter a whole number. \n")

            if not 1 <= user_guess <= max_num:
                print("Out of range. \n")

            tries += 1

            if user_guess > target_num:
                print("Too high")
            elif user_guess < target_num:
                print("Too low")
            else:
                print(f"Correct! You guessed it in {tries} tries \n")
                break
            
        play_again = str(input("Play again? [y/n] \n")).lower()
        if play_again != "y":
            break


if __name__ == "__main__":
    number_guessing_game()