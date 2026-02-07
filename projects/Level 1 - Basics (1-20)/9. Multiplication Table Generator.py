def mult_table_gen():
    while True:
        try:
            user_num: int = int(input("Number: "))
            table_size: int = int(input("Table size: "))
        except ValueError:
            print("\nInvalid Input.")
            continue
        
        if user_num <= 0 or table_size <= 0:
            print("\nThe number and the Table size must be above 0")
            continue
        
        print("------Table------")
        for i in range(1, table_size+1):
            print(f"{user_num} x {i} = {user_num*i}")
        print("-----------------")
        
        if input("\nAgain?  [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    mult_table_gen()