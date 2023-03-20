"""
Temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    """Main function to print menu and print according to the outcome of the choice"""
    print(MENU)
    choice = input(">>> " ).upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = conversion_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = conversion_fahrenhet_to_celsius(fahrenheit)
            print(f"Result {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def conversion_fahrenhet_to_celsius(fahrenheit):
    """This function is to convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


def conversion_celsius_to_fahrenheit(celsius):
    """This function is to convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32

main()
