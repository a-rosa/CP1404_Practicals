"""
Score Menu, get score, print result, print stars as much as scores
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Function is to ask for score and print either menu or stars according to the score"""
    score = get_valid_score()
    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_category(score)
            print(result)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">> ").upper()
    print("Farewell")


def get_valid_score():
    """Function is to get valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_score_category(score):
    """Function is to determine if the score is excellent, passable or bad"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
