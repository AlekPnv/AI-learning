# Import libraries
import random

# Define mostly unchangable variables -> choices, win-conditions, results
choices: list = ["rock", "paper", "scissors"]

wins: dict = {"rock": "scissors", 
       "paper": "rock", 
       "scissors": "paper"}

def rps_game() -> None:
    win = loss = tie = 0
    
    # Start loop
    while True:
        # Ask user for his choice and randomise the computers choice
        print("---------------------------------------")
        user_choice: str = input("Choose Rock / Paper / Scissors: ").lower()
        
        if user_choice not in choices:
            print("There is no such option. Try again with one of the given options.\n")
            continue
        
        computer_choice: str = random.choice(choices)
        
        print(f"\nPlayer: {user_choice} vs Computer: {computer_choice}")
        
        # Game logic & Results        
        if user_choice == computer_choice:
            print("It's a tie!")
            tie += 1
        elif wins[computer_choice] == user_choice: # wins[computer_choice] = key, user_choice = value
            print("Player lost!")
            loss += 1
        else:
            print("Player wins!")
            win += 1
        
        print(f"\nWins: {win} - Losses: {loss} - Ties: {tie}")
        
        # Repeat logic
        if str(input("Again? [y/n]: ")).lower() != "y":
            break
        
        
if __name__ == "__main__":
    rps_game()