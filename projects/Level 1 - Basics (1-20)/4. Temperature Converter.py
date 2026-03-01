def temp_converter():
    while True:
        Units = {"celsius": "c", "fahrenheit": "f", "kelvin": "k"}
        try:
            user_temp = float(input("Enter temperature: "))
        except ValueError:
            print("Try a number")
            continue
        
        print("\nChoose the Unit that you're using from the list")
        for k, v in Units.items():
            print(f"({k} - {v})", end=" | ")
        
        user_unit = input("Enter Original Unit: ").lower()
        if user_unit in Units.keys() or user_unit in Units.values():
            if user_unit in Units.keys():
                del Units[user_unit]
            else:
                Units = {k: v for k, v in Units.items() if v != user_unit}
        else:
            print("Invalid Input - Try again.")
            continue
        
        print("\nIn what Unit should it get converter")
        for k, v in Units.items():
            print(f"({k} - {v})", end=" | ")
        
        try:
            target_unit = input("Enter Target Unit: ").lower()
            
            if target_unit in Units.keys() or target_unit in Units.values():
                print("Converting...\n")
            else:
                raise ValueError
        except ValueError:
            print("Invalid unit. Please choose from the available options above.")
            continue
        
        if user_unit == "c" or user_unit == Units.get("celsius"):
            if target_unit == "fahrenheit" or target_unit == Units.get("fahrenheit"):
                converted_temp = (user_temp * 9/5) + 32
                print(f"{user_temp}°C -> {converted_temp}°F")
            elif target_unit == "kelvin" or target_unit == Units.get("kelvin"):
                converted_temp = user_temp + 273.15
                print(f"{user_temp}°C -> {converted_temp} K")
        elif user_unit == "f" or user_unit == Units.get("fahrenheit"):
            if target_unit == "celsius" or target_unit == Units.get("celsius"):
                converted_temp = (user_temp - 32) * 5/9
                print(f"{user_temp}°F -> {converted_temp}°C")
            elif target_unit == "kelvin" or target_unit == Units.get("kelvin"):
                converted_temp = (user_temp - 32) * 5/9 + 273.15
                print(f"{user_temp}°F -> {converted_temp} K")
        elif user_unit == "k" or user_unit == Units.get("kelvin"):
            if target_unit == "celsius" or target_unit == Units.get("celsius"):
                converted_temp = user_temp - 273.15
                print(f"{user_temp} K -> {converted_temp} °C")
            elif target_unit == "fahrenheit" or target_unit == Units.get("fahrenheit"):
                converted_temp = (user_temp - 273.15) * 9/5 + 32
                print(f"{user_temp} K -> {converted_temp} °F")
        
        repeat = input("\nAgain? [y/n]: ").lower()
        if repeat != "y":
            break

if __name__ == "__main__":
    temp_converter()



