from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    choice = CoffeeMaker()
    menu = Menu()
    drinks_available = menu.get_items()
    pay = MoneyMachine()

    # print(drinks_available)
    # if action == "off":
    #     maintenance_required = True
    #     print("Coffee machine has been turned off for maintenance")
    maintenance_required = False
    while not maintenance_required:
        action = input(f"What would you like? {drinks_available}: ").lower()

        if menu.find_drink(action):
            # gets the info of item, name and ingr for the drink
            item = menu.find_drink(action)
            drink_name = item.name
            drink_cost = item.cost
            water_required, milk_required, coffee_required = item.ingredients["water"], item.ingredients["milk"], \
                                                             item.ingredients["coffee"]
            # print(f"ingredients = {water_required, milk_required, coffee_required}")
        if action == "off":
            maintenance_required = True
            print("Coffee machine has been turned off for maintenance")
            return
        elif action == "report":
            # publish_report()
            choice.report()
            pay.report()
        else:
            # checking resources if drink can be made or not
            if choice.is_resource_sufficient(item) and pay.make_payment(drink_cost):
                # if yes, process coins,
                # if coins processed, make coffee
                choice.make_coffee(item)


coffee_machine()
