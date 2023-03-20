DISCOUNT = 0.9
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_price = 0
for item in range(number_of_items):
    price_item = float(input("Price of item: "))
    total_price += price_item
if total_price > 100:
    total_price *= DISCOUNT
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
