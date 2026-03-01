def get_values(prompt) -> float:
    while True:
        num = input(prompt)
        try:
            num = float(num)

            if num <= 0:
                print("Invalid Number! Must be greater than 0")
                continue

            return num

        except ValueError:
            print("Invalid Input! Must enter a valid number")


def calculate_interest(amount: float, rate: float, time: float) -> tuple[float, float]:
    interest = (amount * rate * time) / 100
    total_amount = amount + interest
    return interest, total_amount  # fixed: was returning (total_amount, interest) — swapped


def main():
    while True:
        amount = get_values("Initial amount: ")
        annual_rate = get_values("Annual interest rate (%): ")
        num_years = get_values("Time in years: ")

        interest, total_amount = calculate_interest(amount, annual_rate, num_years)

        print(f"\nInterest earned: {interest:.2f}€")
        print(f"Total amount:    {total_amount:.2f}€")

        if input("\nAgain? [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    main()
