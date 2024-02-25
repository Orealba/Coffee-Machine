from logo import logo_machine
from logo import logo_coffee
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


"""HOW MANY INGREDIENTS"""


def ingredients_verification(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    for ingredient, quantity in ingredients.items():
        if resources[ingredient] < quantity:

            return False
    return True


def ingredients_subtract(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    for ingredient, quantity in ingredients.items():
        resources[ingredient] -= quantity

def ingredients_adding():
    for ingredient, quantity in resources.items():
        resources[ingredient] += 300


"""ADDING COINS"""


def calculate_coins(pennies, nickels, dimes, quarters):
    adding = 0
    adding += 0.01 * pennies
    adding += 0.05 * nickels
    adding += 0.10 * dimes
    adding += 0.25 * quarters
    return round(adding, 2)


"""SHOW ME THE MONEY"""


def give_me_money(drink_name, your_money):
    price = MENU[drink_name]["cost"]
    if price > your_money:
        return False
    return True


def resources_left():
    for ingredient, quantity in resources.items():
        print(ingredient, ":",  quantity)


def coffee_machine():
    money_machine = 0
    print(logo_machine)
    while True:
        user_input = input("Welcome. What would you like? Type 1 for Espresso, 2 for Latte or 3 for Cappuccino: ")

        drink_options = {
            "1": "espresso",
            "2": "latte",
            "3": "cappuccino"
        }

        drink_name = drink_options.get(user_input)
        if drink_name:
            if ingredients_verification(drink_name):
                coffee_price = MENU[drink_name]["cost"]
                print("This cost:$", coffee_price, "please insert the coins.")
                pennies = int(input("How many pennies?: "))
                nickels = int(input("How many nickels?: "))
                dimes = int(input("How many dimes?: "))
                quarters = int(input("How many quarters?: "))

                total_money = calculate_coins(pennies, nickels, dimes, quarters)

                if give_me_money(drink_name, total_money):
                    money_machine += coffee_price
                    ingredients_subtract(drink_name)
                    print(f"Perfect, your change is:$", round(total_money - coffee_price, 2), "Here is your", drink_name, "☕️ enjoy!", logo_coffee)

                else:
                    print("This is not enough money, came back latter with more coins.")
            else:
                print("I don't have enough ingredients, come back later.Sorry")
        elif user_input == "report":
            print("Currently this is what I have:")
            resources_left()
            print("money in the machine:$", money_machine)
        elif user_input == "recharge":
            print("loaded, now this is my ingredients list currently:")
            ingredients_adding()
            resources_left()

        elif user_input == "stop":
            break


coffee_machine()


# TODO: 1. Type of coffee do you want? ✔
# TODO: 2. check all coffee's ingredients it has for that choices of coffee.✔
# TODO: 3. No ingredients, say bye.
# TODO: 4. All ingredients: How many coins do you have? ask every coin.✔
# TODO: 5. Adding all coins, calculate if it is correct, need change or not, and if it isn't enough money, say bye.✔ X
# TODO: 6. Make the coffee, rest the ingredients, calculate the change if it need it and give the coffee and change.✔
# TODO: 7. Secret key for report status.✔
