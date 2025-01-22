from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
my_money_machine=MoneyMachine()
my_coffee=CoffeeMaker()
menu=Menu()
choice= input('which one would you like: latte , cappuccino or espresso? ')
while choice != 'off':
    if choice=='report':
        my_money_machine.report()
        my_coffee.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
                my_coffee.make_coffee(drink)
    choice = input('which one would you like: latte , cappuccino or espresso? ')



