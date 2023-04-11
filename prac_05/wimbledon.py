"""
Game, Set, Match
estimate: 30 mins
actual: 25 mins
"""

def main():
    """Read the wimbledon csv file and display the champions and how many times they won and the country in
    alphabetical order """
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        winners = {}
        country_of_winners = []
        # start reading from the second line
        datas = in_file.readlines()[1:]
        for data in datas:
            get_winner_occurrences(data, winners)
            get_winning_country_list(country_of_winners, data)
        print_winners_list(winners)
        print()
        country_of_winners.sort()
        print_country_of_winners_list(country_of_winners)


def print_country_of_winners_list(country_of_winners):
    """Print the country of winners list"""
    print(f"These {len(country_of_winners)} countries have won Wimbledon:")
    print(", ".join(country_of_winners))


def print_winners_list(winners):
    """Print the winners and how many they have won"""
    print("Wimbledon Champions:")
    for winner in winners.items():
        print(f"{winner[0]} {winner[1]}")


def get_winning_country_list(country_of_winners, data):
    """Get the country where the winner is from and list them"""
    country = data.split(",")[1]
    if country not in country_of_winners:
        country_of_winners.append(country)


def get_winner_occurrences(data, winners):
    """Get winner name and how many they have won"""
    winner_name = data.split(",")[2]
    if winner_name in winners:
        winners[winner_name] += 1
    else:
        winners[winner_name] = 1


main()
