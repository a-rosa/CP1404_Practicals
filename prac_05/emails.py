"""
Emails
estimate: 30 mins
actual: 30 mins
"""

def main():
    email_details = {}
    email = input("Email: ")

    while email != "":
        name = get_name(email)
        correctness = input(f"Is your name {name}? (Y/N) ").upper()
        if correctness != "" and correctness != "Y":
            name = input("Name: ").title()
        email_details[name] = email
        email = input("Email: ")
    print()

    for detail in email_details.items():
        print(f"{detail[0]} ({detail[1]})")

def get_name(email):
    name = " ".join(email.split("@")[0].split(".")).title()
    return name

main()