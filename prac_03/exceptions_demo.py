"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the user does not input an integer
2. When will a ZeroDivisionError occur? When the user enters a 0 in the denominator
   and when the program tries to divide something with zero, the error would occur
3. Could you change the code to avoid the possibility of a ZeroDivisionError? By repeatedly asking for a valid number
"""

def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = get_valid_denominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def get_valid_denominator():
    number = int(input("Enter the denominator: "))
    while number == 0:
        print("Denominator can't be 0")
        number = int(input("Enter the denominator: "))
    return number

main()