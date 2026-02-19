def withdraw(amount: float, balance: float) -> float:
    return balance - amount


def deposit(amount: float, balance: float) -> float:
    return balance + amount


def main():
    user_balance: float = 1000.0

    while True:
        print("------ ATM ------")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        try:
            choice = int(input("\nChoose an option [1-4]: "))
        except ValueError:
            print("Invalid input. Try a number.\n")
            continue

        if choice == 1:
            print(f"Balance: {user_balance:.2f}€")

        elif choice == 2:
            try:
                amount = float(input("Deposit amount: "))
                if amount <= 0:
                    print("Amount must be greater than 0\n")
                    continue
                user_balance = deposit(amount, user_balance)
                print(f"New balance: {user_balance:.2f}€")
            except ValueError:
                print("Invalid number\n")

        elif choice == 3:
            try:
                amount = float(input("Withdraw amount: "))
                if amount <= 0:
                    print("Amount must be greater than 0\n")
                    continue
                if amount > user_balance:
                    print("Insufficient funds\n")
                    continue
                user_balance = withdraw(amount, user_balance)
                print(f"New balance: {user_balance:.2f}€")
            except ValueError:
                print("Invalid number\n")

        elif choice == 4:
            print("Closing...")
            break

        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()
