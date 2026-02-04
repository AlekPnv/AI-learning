def even_odd_checker():
    while True:
        print("--------------------------")
        try:
            if int(input("Type a whole number: ")) % 2:
                print ("Your nubmer is Odd")
            else: 
                print("Your number is Even")
        except ValueError:
            print("Error! Whole number expected.")
        
        if str(input("\nAgain? [y/n]: ")).lower() != "y":
            break

if __name__ == "__main__":
    even_odd_checker()