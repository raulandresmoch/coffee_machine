from dictionaries import MENU, resources

# TODO : Print a report of resources


def report(water, milk, coffee, money):
    print(f"Water : {water} ml ")
    print(f"Milk : {milk} ml ")
    print(f"Coffee : {coffee} g ")
    print(f"Money : ${money} ")

# TODO 2: Check resources is sufficient


def check_resources(water, milk, coffee):
    if water > MENU[user_drink]['ingredients']['water'] and milk > MENU[user_drink]['ingredients']['milk'] and coffee > \
            MENU[user_drink]['ingredients']['coffee']:
        return True
    else:
        return False

# TODO 3: Process Coins


def money_paid(quarters, dimes, nickles, cents):
    quarters_paid = quarters * .25
    dimes_paid = dimes * .10
    nickles_paid = nickles * .05
    cents_paid = cents * .01
    total_paid = quarters_paid + dimes_paid + nickles_paid + cents_paid
    return total_paid


water = 300
milk = 200
coffee = 100
money = 0
machine_working = True

while machine_working == True:
    user_drink = input("What would you like to drink (espresso, latte, cappuccino): ").lower()
    if user_drink == "report":
        report(water, milk, coffee, money)
        break
    else:
        check_resources(water, milk, coffee)

    if check_resources(water, milk, coffee):
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickles? "))
        cents = float(input("How many cents? "))
    else:
        print("Sorry I don't have enough resources to process that Drink.")

    # print(money_paid(quarters, dimes, nickels, cents))

    # TODO 4: Check Transaction Successful

    if money_paid(quarters, dimes, nickels, cents) > MENU[user_drink]['cost']:
        change = round(money_paid(quarters, dimes, nickels, cents) - MENU[user_drink]['cost'],2)
        print(f"Here is ${change} in change")
        print(f"Enjoy your {user_drink}!!")
        money += round(money_paid(quarters, dimes, nickels, cents) - change)
        water -= MENU[user_drink]['ingredients']['water']
        milk -= MENU[user_drink]['ingredients']['milk']
        coffee -= MENU[user_drink]['ingredients']['coffee']
    else:
        print(f"Not enough money paid, here is your {money_paid()}")
    # TODO 5: Make Coffee

