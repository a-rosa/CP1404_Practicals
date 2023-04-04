import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
AMOUNT_IN_A_PICK = 6

quick_pick = int(input("How many quick picks: "))

numbers = [number for number in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1)]
for counter in range(quick_pick):
    picked_numbers = []
    for number_of_times in range(AMOUNT_IN_A_PICK):
        random_index = random.randint(0, len(numbers)-1)
        picked_numbers.append(numbers[random_index])
        numbers.remove(numbers[random_index])
    picked_numbers = sorted(picked_numbers)
    for number in picked_numbers:
        print(f"{number:>2}", end=" ")
    print()
