from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

kofi = CoffeeMaker
moni = MoneyMachine
menu = Menu

def bootup():
    """Initiates the startup of the machine and fills with resources"""
    print("Coffee Machine on\n")
    kofi.__init__(kofi)
    moni.__init__(moni)
    menu.__init__(menu)

def interpreter(expression):
    if expression[:1] == "l":
        return "latte"
    elif expression[:1] == "e":
        return "espresso"
    elif expression[:1] == "c":
        return "cappuccino"
    else:
        return "Invalid input"

is_on = True
bootup()


while is_on:
    try:
        command = str(input(f"What would you like? ({menu.get_items(menu)}): ").lower())
    except:print("Please input a command in the form of a string of text only.")

    if command[:1] == "o":
        print("Shutting down..")
        is_on = False
        exit()
    elif command[:1] == "r":
        kofi.report(kofi)
        moni.report(moni)
    else:
        drink = menu.find_drink(menu,interpreter(command))
        if not drink:
            continue
        else:
          if kofi.is_resource_sufficient(kofi,drink):
              print("True")
              #would like to format the drink cost to reflecct monetary syntax
              monetary_rep = "${:.2f}"
              print(f"{drink.name}: {monetary_rep.format(drink.cost)}")
              moni.make_payment(moni,drink.cost)


        


