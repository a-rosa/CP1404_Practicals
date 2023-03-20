def main():
    score = float(input("Enter score: "))
    category = determine_score_category(score)
    if category == False:
        print("Invalid score")
    else:
        print(category)


def determine_score_category(score):
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