import random

def main():
    while True:
        user_input = input("Enter names (separated by commas): ")
        
        names_list = [name.strip() for name in user_input.split(",") if name.strip()]
        
        while True:
            if len(names_list) < 2:
                print("Atleast 2 names required\n")
                break

            selected_name = random.choice(names_list)

            print(f"Selected name: {selected_name}\n")
            
            names_list.remove(selected_name)

            if input("Select another name? [y/n]: ").lower() != "y":
                break
        
        if input("Restart Program? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    main()