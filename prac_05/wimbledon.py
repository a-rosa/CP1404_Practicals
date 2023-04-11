"""
Game, Set, Match
estimate: 30 mins
actual: 25 mins
"""

def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        winners = {}
        country_of_winners = []
        datas = in_file.readlines()[1:]
        for data in datas:
            get_winner_occurences(data, winners)
            get_winning_country_list(country_of_winners, data)
        print_winners_list(winners)
        print()
        country_of_winners.sort()
        print_country_of_winners_list(country_of_winners)


def print_country_of_winners_list(country_of_winners):
    print(f"These {len(country_of_winners)} countries have won Wimbledon:")
    print(", ".join(country_of_winners))


def print_winners_list(winners):
    print("Wimbledon Champions:")
    for winner in winners.items():
        print(f"{winner[0]} {winner[1]}")


def get_winning_country_list(country_of_winners, data):
    country = data.split(",")[1]
    if country not in country_of_winners:
        country_of_winners.append(country)


def get_winner_occurences(data, winners):
    winner_name = data.split(",")[2]
    if winner_name in winners:
        winners[winner_name] += 1
    else:
        winners[winner_name] = 1


main()
