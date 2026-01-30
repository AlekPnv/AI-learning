def calc():
    while True:
        try:
            num1 = float(input("1.Number: "))
            num2 = float(input("2.Number: "))
        except ValueError:
            print("Invalid Input. Try a number.\n")
            continue
        
        
        operation = str(input("Operator [+ - * /]: "))
        
        
        if num2 == 0 and operation == "/":
            print("Division by Zero is not possible.\n")
            continue
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/" :
            result = num1 / num2
        else:
            print("Invalid Input. Try one of the given options.\n")
            continue
        
        print(f"{num1} {operation} {num2} = {result}\n")
        
        
        repeat = input("Again? [y/n]: ").lower()
        if repeat != "y":
            break


if __name__ == "__main__":
    calc()
