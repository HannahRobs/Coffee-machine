MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

machine_water = 500
machine_milk = 500
machine_coffee = 300

user_drink = ""
total = 0
profit = 0
machine_on = True
fill_me_up = False


def report():
    print(f"Water: {machine_water}ml")
    print(f"Milk: {machine_milk}ml")
    print(f"Coffee: {machine_coffee}g")
    ask_new_drink()
    check_sufficient(user_drink)
    insert_coins()


def ask_new_drink():
    global user_drink
    user_drink = input("What drink would you like? (espresso/ latte/ cappuccino)  ")
    if user_drink == "report":
        report()
    return user_drink


def check_sufficient(user_drink):
    if MENU[user_drink]["ingredients"]["water"] > machine_water:
        print("Not enough water, please fill me up.")
        return False
    elif MENU[user_drink]["ingredients"]["milk"] > machine_milk:
        print("Not enough milk, please fill me up.")
        return False
    elif MENU[user_drink]["ingredients"]["coffee"] > machine_coffee:
        print("Not enough coffee, please fill me up.")
        return False
    else:
        return True


def make_drink(user_drink):
    global machine_water
    global machine_coffee
    global machine_milk
    machine_water -= int(MENU[user_drink]["ingredients"]["water"])
    machine_coffee -= int(MENU[user_drink]["ingredients"]["coffee"])
    machine_milk -= int(MENU[user_drink]["ingredients"]["milk"])
    print(f"Here is your {user_drink}. Enjoy!")
    return machine_coffee, machine_water, machine_milk


def insert_coins():
    print("Please insert coins.")
    a = 0.25 * int(input("How many quarters? "))
    b = 0.10 * int(input("How many dimes? "))
    c = 0.05 * int(input("How many nickles? "))
    d = 0.01 * int(input("How many pennies? "))
    global total
    total = a + b + c + d
    total = round(total, 2)
    print(total)
    return total


while machine_on:
    ask_new_drink()
    if user_drink == 'profit':
        print(f"Total profit is ${profit}.")
        ask_new_drink()
        check_sufficient(user_drink)
        insert_coins()
    if user_drink == 'off':
        machine_on = False
    else:
        if check_sufficient(user_drink):
            insert_coins()
            if total < MENU[user_drink]["cost"]:
                print("Not enough coins, money refunded. Try again")

            elif total > MENU[user_drink]["cost"]:
                change = total - MENU[user_drink]["cost"]
                print(f"Here is your change ${change}.")
                make_drink(user_drink)

    profit += MENU[user_drink]["cost"]





