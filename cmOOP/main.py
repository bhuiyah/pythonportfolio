import coffee_maker
import menu
import money_machine
from os import system


myMenu = menu.Menu()                         #menu are what is required to make the coffee
myCoffeeMaker = coffee_maker.CoffeeMaker()   #coffeeMaker is the ingredients that I have in stock
myMoney = money_machine.MoneyMachine()

def processPurchase(choice):
    system('clear')
    if myCoffeeMaker.is_resource_sufficient(choice) and myMoney.make_payment(choice.cost):
        myCoffeeMaker.make_coffee(choice)

while 1: 
    choice = input("What would you like? (espresso/latte/cappuccino/report): ")
    if choice == "report":
        system('clear')
        myCoffeeMaker.report()
        myMoney.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        find = myMenu.find_drink(choice)
        processPurchase(find)
    elif choice == "off":
        system('clear')
        break
    else:
        print("Invalid Input.")