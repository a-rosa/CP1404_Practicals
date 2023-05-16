from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [prius, limo, hummer]
    bill = 0.00
    taxi_chosen = False
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi available:")
            for index in range(len(taxis)):
                print(f"{index} - {taxis[index]}")
            current_taxi = int(input("Chosen taxi: "))
            if current_taxi < 0 or current_taxi > len(taxis) - 1:
                print("Invalid taxi choice")
                taxi_chosen = False
            else:
                taxi_chosen = True
        elif choice == "d":
            if not taxi_chosen:
                print("You need to choose a taxi before you can drive")
            else:
                drive_distance = int(input("Drive how far? "))
                taxis[current_taxi].start_fare()
                taxis[current_taxi].drive(drive_distance)
                print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare():.2f}")
                bill += taxis[current_taxi].get_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    for index in range(len(taxis)):
        print(f"{index} - {taxis[index]}")


main()
