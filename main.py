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
    """Helps to define user input as menu items based off of array slice"""
    if expression[:1] == "l":
        return "latte"
    elif expression[:1] == "e":
        return "espresso"
    elif expression[:1] == "c":
        return "cappuccino"
    else:
        return "Invalid input"

#Coffee Maching Starts up
is_on = True
bootup()

#Prompts user for initial input
while is_on:
    
    command = str(input(f"What would you like? ({menu.get_items(menu)}): ").lower())
    

    if command[:1] == "o":
        print("Shutting down..")
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
              
              #helps to represent values in a monetary format
              monetary_rep = "${:.2f}"

              print(f"{drink.name}: {monetary_rep.format(drink.cost)}")
              
              #if we have enoguh money we kmake the drink otherwise we start over
              if moni.make_payment(moni,drink.cost):
                kofi.make_coffee(kofi,drink)
              else: 
                continue
              

        


