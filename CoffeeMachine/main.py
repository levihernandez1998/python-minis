import art
import helper
import time

MENU = helper.MENU
COIN = helper.COIN
resources = helper.resources
is_on = True

def start():
    global is_on

    print(art.logo)

    while is_on:
        prompt = get_prompt()
        while prompt is None:
            prompt = get_prompt()

        if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
            get_coffee(prompt)
        elif prompt == "report":
            get_report()
        elif prompt == "settings":
            update_setting()
        elif prompt == "withdraw":
            withdraw_money()
        elif prompt == "off":
            print(art.offline)
            is_on = False

def get_coffee(coffee):
    if check_resources(coffee):
        money = get_money()
        if check_money(coffee, money):
            process_coffee(coffee, money)

def get_report(with_money: bool = True):
    for item_key, item_value in resources.items():
        if not with_money and item_key == "money":
            continue

        if item_key == "money":
            formatted_value = f"${item_value}"
        elif item_key == "coffee":
            formatted_value = f"{item_value}g"
        else:
            formatted_value = f"{item_value}ml"
        print(f"{item_key}: {formatted_value}")

def get_prompt():
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if (prompt == "espresso" or
        prompt == "latte" or
        prompt == "cappuccino" or
        prompt == "report" or
        prompt == "settings" or
        prompt == "withdraw" or
        prompt == "off"):
        return prompt
    else:
        print("Please enter either 'espresso' or 'latte' or 'cappuccino'")
        return None

def get_money():
    penny = int(input("Pennies in hand: "))
    nickel = int(input("Nickels in hand: "))
    dime = int(input("Dime in hand: "))
    quarter = int(input("Quarter in hand: "))
    return ((penny * COIN["penny"]) +
            (nickel * COIN["nickel"]) +
            (dime * COIN["dime"]) +
            (quarter * COIN["quarter"]))

def check_resources(coffee):
    coffee = MENU[coffee]
    for item_key, item_value in coffee["ingredients"].items():
        if item_value > resources[item_key]:
            print(f"\n{art.missing}\n")
            print(f"Sorry, that's not enough {item_key}\n")
            return False
    return True

def check_money(coffee, money):
    coffee = MENU[coffee]
    if coffee["cost"] > money:
        print(f"\nSorry, you don't have enough money. Total cost is ${coffee['cost']}💸\n")
        return False
    return True

def process_coffee(coffee, money):
    coffee = MENU[coffee]
    change = round(money - coffee["cost"], 2)

    resources["money"] += money
    for item_key, item_value in coffee["ingredients"].items():
        if item_value <= resources[item_key]:
            resources[item_key] -= item_value

    print(f"\n [[ Your total change is ${change}✨ Enjoy your coffee! ☕ ]]\n")

def update_setting():
    resources["water"] += int(input("Water: "))
    resources["milk"] += int(input("Milk: "))
    resources["coffee"] += int(input("Coffee: "))
    print("Resources updated! 🔍")
    get_report(False)

def withdraw_money():
    if resources["money"] <= 0:
        print("There's nothing to withdraw 💸\n")
    else:
        print("Withdrawing...🔃")
        time.sleep(2)

        resources["money"] = 0
        print("All coins has been withdrawn ✅\n")


start()