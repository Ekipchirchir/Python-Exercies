# define the menu as a dictionary of items and prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# initialize the total cost to 0
total_cost = 0

# prompt the user for input until they press control-d
while True:
    try:
        # prompt the user for an item
        item = input("Enter an item: ").title()

        # if the item is not on the menu, ignore it
        if item not in menu:
            continue

        # add the item's price to the total cost
        total_cost += menu[item]

        # display the total cost so far
        print(f"Total cost: ${total_cost:.2f}")

    except EOFError:
        # if the user presses control-d, exit the loop
        break