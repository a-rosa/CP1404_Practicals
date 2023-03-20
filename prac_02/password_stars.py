"""
Get password and turn them into stars according to their length
"""

MINIMUM_LENGTH = 8


def main():
    """Main function is to get password and output password as stars"""
    password = get_password()
    print_password_to_stars(password)


def print_password_to_stars(password):
    """This function is to print stars with the same length as password"""
    print("Password:", "*" * len(password))


def get_password():
    """This function is to get valid password"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Minimum length not met")
        password = input("Enter password: ")
    return password

main()