"""
Get score and return either excellent, passable, bad or invalid
"""

def main():
    """Get score and print result"""
    from random import randint
    score = float(input("Enter score: "))
    category = determine_score_category(score)
    if category == False:
        print("Invalid score")
    else:
        print(category)
    score = randint(0,100)
    category = determine_score_category(score)
    print(f"Random score: {score}")
    print(f"Result: {category}")


def determine_score_category(score):
    """This function would determine the category depending on the score"""
    if score < 0 or score > 100:
        return False
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"

main()