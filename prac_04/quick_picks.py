import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
AMOUNT_IN_A_PICK = 6

quick_pick = int(input("How many quick picks: "))

numbers = [number for number in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1)]
for counter in range(quick_pick): # Go through all the quick picks user inputs
    picked_numbers = []
    for number_of_times in range(AMOUNT_IN_A_PICK): # Loop six times to get 6 random numbers in one pick
        random_index = random.randint(0, len(numbers)-1) # Get random index from the numbers list that has different length each time
        picked_numbers.append(numbers[random_index]) # Append first the number in the index of the numbers list
        numbers.remove(numbers[random_index]) # Delete that number from the numbers list, so the length changes
    picked_numbers = sorted(picked_numbers)
    for number in picked_numbers:
        print(f"{number:>2}", end=" ")
    print()
