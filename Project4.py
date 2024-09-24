# Temperature Converter Program

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0/5.0 + 32
    return fahrenheit

def main():
    print("Temperature Converter Program")
    print("-------------------------------")

    while True:
        print("Choose a conversion direction:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        else:
            print("Invalid choice. Please try again.")

        cont = input("Do you want to continue? (YES/NO): ")
        if cont.lower() != "YES":
            break

if __name__ == "__main__":
    main()