from resources import MENU, resources
from os import system

def processPurchase(choice):
    system('clear')
    res_needed = MENU[choice]["ingredients"]
    flag = 1
    for ing in res_needed:
        if res_needed[ing] > resources[ing]:
            print(f"Sorry there is not enough {ing}.")
            flag = 0
    
    if flag:
        print("Please insert coins.")
        quartamt = int(input("How many quarters?: "))
        dimamt = int(input("How many dimes?: "))
        nickamt = int(input("How many nickles?: "))
        penamt = int(input("How many pennies?: "))

        totalamt = quartamt * 0.25 + dimamt * 0.10 + nickamt * 0.05 + penamt * 0.01

        if(totalamt < MENU[choice]["cost"]):
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["money"] += MENU[choice]["cost"]
            change = round(totalamt - MENU[choice]["cost"], 2)
            print(f"Here is ${change:.2f} in change.")
            for ing in res_needed:
                resources[ing] -= res_needed[ing]
            print(f"Enjoy your {choice}☕!")


def report():
    system('clear')
    for resource in resources:
        if(resource == "money"):
            print(f"{resource.title()}: ${resources[resource]:.2f}")
        elif(resource == "water" or resource == "milk"):
            print(f"{resource.title()}: {resources[resource]}ml")
        elif(resource == "coffee"):
            print(f"{resource.title()}: {resources[resource]}g")

while 1: 
    choice = input("What would you like? (espresso/latte/cappuccino/report): ")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        processPurchase(choice)
    elif choice == "report":
        report()
    elif choice == "off":
        system('clear')
        break
    else:
        print("Invalid Input.")