
Appetizers = ["Wings", "Cookies", "Spring Rolls"]
Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream", "Cake", "Pie"]
Drinks = ["Coffee", "Tea", "Unicorn Tears"]


def menu():
    print("*"*39)
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type 'quit' **")
    print("*"*39)
    print("-" * 11)
    print("Appetizers")
    print("-"*11)
    for i in Appetizers:
        print(i)
    print("-" * 11)
    print("Entrees")
    print("-"*11)
    for i in Entrees:
        print(i)
    print("-" * 11)
    print("Desserts")
    print("-"*11)
    for i in Desserts:
        print(i)
    print("-" * 11)
    print("Drinks")
    print("-"*11)
    for i in Drinks:
        print(i)

    print("*"*39)
    print("** What would you like to order? **")
    print("*" * 39)

    count = 0
    new_order = input(">")
    menu_customer = []

    while new_order != "quit":
        if new_order in Appetizers or new_order in Entrees or new_order in Desserts or new_order in Drinks:
            count += 1
            menu_customer.append(new_order)
            print(f"** {menu_customer.count(new_order)} order of {new_order} has been added to your meal **")
            new_order = input(">")
        else:
            print("Not in the menu")
            new_order = input(">")


menu()
