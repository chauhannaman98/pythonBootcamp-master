from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

isOn = True

while isOn:
    order_name = input(f"What would you like? ({menu.get_items()}): ")
    if order_name == "off":
        isOn = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
