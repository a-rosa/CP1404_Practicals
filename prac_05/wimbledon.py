"""
Game, Set, Match
estimate: 30 mins
actual: 25 mins
"""

with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    winners = {}
    country_of_winners = []
    column_name = in_file.readline()
    datas = in_file.readlines()
    for data in datas:
        winner_name = data.split(",")[2]
        if winner_name in winners:
            winners[winner_name] += 1
        else:
            winners[winner_name] = 1
        country = data.split(",")[1]
        if country not in country_of_winners:
            country_of_winners.append(country)
    print("Wimbledon Champions:")
    for winner in winners.items():
        print(f"{winner[0]} {winner[1]}")
    print()
    country_of_winners.sort()
    print(f"These {len(country_of_winners)} countries have won Wimbledon:")
    print(", ".join(country_of_winners))
