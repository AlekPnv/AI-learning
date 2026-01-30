import random

def dice_simulator():
    # --- Simulation loop ---
    while True:
        # --- Input ---
        try:
            dice_sides = int(input("Dice sides: "))
            num_of_rolls = int(input("Number of rolls: "))
        except ValueError:
            print("That was no valid number.  Try again...\n")

        if dice_sides < 2 or num_of_rolls <= 0:
            print("Dice must have at least 2 sides and rolls must be positive.\n")
            continue
            
        # --- Simulation
        possible_nums = [num+1 for num in range(dice_sides)] # all the numbers up to the wished sides of dice - 6 sides = 6 numbers
        results = {num: 0 for num in possible_nums} # num: 0... instead (num for num in possible_nums): 0
        # or just -> results = {num: 0 for num in range(1, dice_sides + 1)}

        for _ in range(num_of_rolls):
            rolled_num = random.randint(1, dice_sides)
            results[rolled_num] += 1 # -> dic["keys"] += "value"

        # --- Output ---
        print("\nResults: ")
        for k, v in results.items(): # iterate through the keys and values of the dictionary
            print(f"{k} -> {v} {'time' if v == 1 else 'times'}")

        most_common_roll = max(results, key=results.get)
        print(f"\nMost common roll: {most_common_roll}")
        
        # --- Repeat ---
        repeat = input("\nAgain? [y/n]: ").lower()
        if repeat != "y":
            break

if __name__ == "__main__":
    dice_simulator()
