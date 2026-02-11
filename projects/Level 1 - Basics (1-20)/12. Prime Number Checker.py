import math

def prime_num_checker():
    while True:
        try:
            print("----------------")
            num = int(input("Number: "))
        except ValueError:
            print("Invalid Input! Only whole numbers accepted.")
            continue
        
        if num < 2:
            print("Number must be above 1")
            continue
        
        factors = []
        is_prime = True
        
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(int(i))
        
        is_prime = len(factors) == 2
        
        if is_prime == True:
            print("Number is a prime")
        else:
            print("Number isn't a prime")

        print(f"\nAll factors of {num}: ")
        print(", ".join(map(str, factors)))

        if input("\nAgain? [y/n]: ").lower() != "y":
            break

if __name__ == "__main__":
    prime_num_checker()