def main():
    while True:
        user_data = user_input()
        number, unit = user_data
        unit = unit.lower()
        if unit =="c":
            result = c_to_f(number)
            print(f"{number}°C -> {result:.2f}°F")
        elif unit == "f":
            result = f_to_c(number)
            print(f"{number}°F -> {result:.2f}°C")
        else:
            print("Invalid unit! Use C or F only.")
            continue

        again = input("\nConvert Another? (y/n): ").lower()
        if again != 'y':
            print("Exiting...")
            break

def user_input():
    while True:
        user_in = input("Enter Temperature(Example: 25 C): ")
        if not user_in:
            print("Input Can't be empty!!!")
            continue
        parts = user_in.split()
        if len(parts) != 2:
            print("Please enter in format: value unit (ex: 25 C)")
            continue
        number, unit = parts

        try:
            number = float(number)
        except ValueError:
            print("Temperature Must be a number!!!")
            continue
        return number,unit
    

def c_to_f(c):
    return c *(9/5) + 32

def f_to_c(f):
    return (f -32) * 5/9


if __name__ == "__main__":
    main()