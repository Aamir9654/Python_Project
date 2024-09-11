
print("hello world")

MENU={
    "espresso":{
        "ingredients":{
        "water": 50,
        "coffee" : 18
    },
    "cost" : 1.5,
},
"latte":{
        "ingredients":{
        "water": 200,
        "coffee" : 24,
        "milk" : 150
    },
    "cost" : 2.5,
},
"cappuccino":{
        "ingredients":{
        "water": 250,
        "coffee" : 24,
        "milk" : 100
    },
    "cost" : 3.5,
},
}
profit  =0

resources ={
    "water":300,
    "milk": 200,
    "coffee":100
}

def is_resource_sufficient(order_ingrdients):

    for item in order_ingrdients:
        if order_ingrdients[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True

def process_coin():

    print("Please insert coins? :")
    total = int(input("how many quarter?:")) * 0.25
    total += int(input("how many dimes? :")) * 0.1
    total += int(input("how many nickles? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01

    return total
def is_transaction_sucessful(money_received, drink_cost):
    '''return true when payment is accepted, or false if money is insufficient'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    """deduct the reuired ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']} ml")
       print(f"Milk: {resources['milk']} ml")
       print(f"Coffee: {resources['coffee']} ")
       print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_sucessful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])