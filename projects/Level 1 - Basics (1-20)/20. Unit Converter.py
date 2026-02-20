def convert_units(value: float, from_unit: str, to_unit: str):
    length_factors = {
        "meters": 1,
        "centimeters": 0.01,
        "kilometers": 1000,
        "miles": 1609.34,
    }
    
    weight_factors = {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
    }
    
    if from_unit in length_factors and to_unit in length_factors:
        # convert value to base length unit (meters)
        value_in_base = value * length_factors[from_unit]

        # convert value from base length unit to the desired unit
        converted_value = value_in_base / length_factors[to_unit]

        return converted_value
    elif from_unit in weight_factors and to_unit in weight_factors:
        # convert value to base weight unit (kilograms)
        value_in_base = value * weight_factors[from_unit]

        # convert value from base weight unit to the desired unit
        converted_value = value_in_base / weight_factors[to_unit]

        return converted_value
    else:
        if from_unit == "C":
            if to_unit == "F":
                converted_value = value * 1.8 + 32
                return converted_value
            elif to_unit == "K":
                converted_value = value + 273.15
            else:
                return value
        
        elif from_unit == "F":
            if to_unit == "C":
                converted_value = (value - 32) / 1.8
                return converted_value
            elif to_unit == "K":
                converted_value = (value + 459.67) * 5 / 9
                return converted_value
            else:
                return value
        
        elif from_unit == "K":
            if to_unit == "C":
                converted_value = value - 273.15
                return converted_value
            elif from_unit == "F":
                converted_value = value * 9 / 5 - 459.67
                return converted_value
            else:
                return value
        
        else:
            return value

def main():
    while True:
        print("----- Unit Converter Menu -----")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        try:
            user_input = int(input("\nChoose an option [1-4]: "))
        except ValueError:
            print("Must be a whole number")
            continue
        
        if user_input == 1:
            while True:
                print("\n----- Length Converter -----")
                print("1. Meters to Kilometers")
                print("2. Meters to Centimeters")
                print("3. Meters to Miles")
                print("4. Kilometers to Miles")
                print("5. Kilometers to Centimeters")
                print("6. Kilometers to Meters")
                print("7. Centimeters to Kilometers")
                print("8. Centimeters to Miles")
                print("9. Centimeters to Meters")
                print("10. Miles to Kilometers")
                print("11. Miles to Centimeters")
                print("12. Miles to Meters")

                try:
                    user_conversion_type = int(input("\nChoose an option [1-12]: "))
                except ValueError:
                    print("Try one of the given numbers")
                    continue

                if user_conversion_type and user_conversion_type in range(1, 13):
                    try:
                        unit_value = float(input("\nEnter value: "))
                    except ValueError:
                        print("Must be a number")
                        continue
                    
                    if user_conversion_type == 1:
                        result = convert_units(unit_value, "meters", "kilometers")
                        print(f"Result: {result:.2f} km")
                    elif user_conversion_type == 2:
                        result = convert_units(unit_value, "meters", "centimeters")
                        print(f"Result: {result:.2f} cm")
                    elif user_conversion_type == 3:
                        result = convert_units(unit_value, "meters", "miles")
                        print(f"Result: {result:.2f} mi")
                    elif user_conversion_type == 4:
                        result = convert_units(unit_value, "kilometers", "miles")
                        print(f"Result: {result:.2f} mi")
                    elif user_conversion_type == 5:
                        result = convert_units(unit_value, "kilometers", "centimeters")
                        print(f"Result: {result:.2f} cm")
                    elif user_conversion_type == 6:
                        result = convert_units(unit_value, "kilometers", "meters")
                        print(f"Result: {result:.2f} m")
                    elif user_conversion_type == 7:
                        result = convert_units(unit_value, "centimeters", "kilometers")
                        print(f"Result: {result:.2f} km")
                    elif user_conversion_type == 8:
                        result = convert_units(unit_value, "centimeters", "miles")
                        print(f"Result: {result:.2f} mi")
                    elif user_conversion_type == 9:
                        result = convert_units(unit_value, "centimeters", "meters")
                        print(f"Result: {result:.2f} m")
                    elif user_conversion_type == 10:
                        result = convert_units(unit_value, "miles", "kilometers")
                        print(f"Result: {result:.2f} km")
                    elif user_conversion_type == 11:
                        result = convert_units(unit_value, "miles", "centimeters")
                        print(f"Result: {result:.2f} cm")
                    elif user_conversion_type == 12:
                        result = convert_units(unit_value, "miles", "meters")
                        print(f"Result: {result:.2f} m")
                    
                else:
                    print("Try one of the given options")
                    continue
                
                print()
                break
        
        elif user_input == 2:
            while True:
                print("\n----- Weight Converter -----")
                print("1. Kilograms to Grams")
                print("2. Kilograms to Pounds")
                print("3. Grams to Kilograms")
                print("4. Grams to Pounds")
                print("5. Pounds to Kilograms")
                print("6. Pounds to Grams")

                try:
                    user_conversion_type = int(input("\nChoose an option [1-6]: "))
                except ValueError:
                    print("Try one of the given numbers")
                    continue
                
                if user_conversion_type and user_conversion_type in range(1,7):
                    try:
                        unit_value = float(input("\nEnter value: "))
                    except ValueError:
                            print("Must be a number")
                            continue
                    
                    if user_conversion_type == 1:
                        result = convert_units(unit_value, "kilograms", "grams")
                        print(f"Result: {result:.2f} g")
                    elif user_conversion_type == 2:
                        result = convert_units(unit_value, "kilograms", "pounds")
                        print(f"Result: {result:.2f} lb")
                    elif user_conversion_type == 3:
                        result = convert_units(unit_value, "grams", "kilograms")
                        print(f"Result: {result:.2f} kg")
                    elif user_conversion_type == 4:
                        result = convert_units(unit_value, "grams", "pounds")
                        print(f"Result: {result:.2f} lb")
                    elif user_conversion_type == 5:
                        result = convert_units(unit_value, "pounds", "kilograms")
                        print(f"Result: {result:.2f} kg")
                    elif user_conversion_type == 6:
                        result = convert_units(unit_value, "pounds", "grams")
                        print(f"Result: {result:.2f} g")

                else:
                    print("Try one of the given options")
                    continue
                    
                print()
                break
                
        elif user_input == 3:
            while True:
                print("\n----- Temperature Converter -----")
                print("1. Celsius to Fahrenheit")
                print("2. Celsius to Kelvin")
                print("3. Fahrenheit to Celsius")
                print("4. Fahrenheit to Kelvin")
                print("5. Kelvin to Fahrenehit")
                print("6. Kelvin to Celsius")
                
                try:
                    user_conversion_type = int(input("\nChoose an option [1-6]: "))
                except ValueError:
                    print("Try one of the given numbers")
                    continue
                
                if user_conversion_type and user_conversion_type in range(1,7):
                    try:
                        unit_value = float(input("\nEnter value: "))
                    except ValueError:
                        print("Must be a number")
                        continue
                    
                    if user_conversion_type == 1:
                        result = convert_units(unit_value, "C", "F")
                        print(f"Result: {result:.2f} F")
                    elif user_conversion_type == 2:
                        result = convert_units(unit_value, "C", "K")
                        print(f"Result: {result:.2f} K")
                    elif user_conversion_type == 3:
                        result = convert_units(unit_value, "F", "C")
                        print(f"Result: {result:.2f} C")
                    elif user_conversion_type == 4:
                        result = convert_units(unit_value, "F", "K")
                        print(f"Result: {result:.2f} K")
                    elif user_conversion_type == 5:
                        result = convert_units(unit_value, "K", "F")
                        print(f"Result: {result:.2f} F")
                    elif user_conversion_type == 6:
                        result = convert_units(unit_value, "K", "C")
                        print(f"Result: {result:.2f} C")

                else:
                    print("Try one of the given options")
                    continue
                    
                print()
                break
        
        
        elif user_input == 4:
            print("Ending...")
            break
        
        else:
            print("Try one of the given options")
            continue


if __name__ == "__main__":
    main()