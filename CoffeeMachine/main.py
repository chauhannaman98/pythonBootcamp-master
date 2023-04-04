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


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def make_drink(drink_ingredients):
    for item in drink_ingredients:
        resources[item] = resources[item] - drink_ingredients[item]


profit = 0
resources = {
    "water": 12000,
    "milk": 6000,
    "coffee": 3000,
}

isOn = True
while isOn:
    choice = input("“What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        resource_sufficient = is_resource_sufficient(drink['ingredients'])
        if resource_sufficient:
            print("Please insert the coins")
            quarters = int(input("Quarter: "))
            dimes = int(input("Dimes: "))
            nickles = int(input("Nickles: "))
            pennies = int(input("Pennies: "))
            inserted_value = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
            if drink['cost'] > inserted_value:
                print("“Sorry that's not enough money. Money refunded.")
            else:
                if drink['cost'] < inserted_value:
                    change = inserted_value - drink['cost']
                    print(f"Here is ${round(change, 2)} dollars in change.")
                profit = profit + drink['cost']
                make_drink(drink['ingredients'])
                print(f"Here is your {choice}. Enjoy!")
