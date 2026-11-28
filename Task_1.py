menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {}

print("===== CANTEEN MENU =====")

for item, price in menu.items():
    print(item, "-", price)

number = int(input("\nEnter number of order attempts: "))

for i in range(1, number):#should be for i in range (1, number + 1)

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    if item in menu:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity < 0:
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)