def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" :add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

logo = '''
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)
def calculator():
    should_continue = True
    first_num = float(input("What is your first number"))
    while should_continue:

        for choose in operations:
            print(choose)
        operation_symbol = input("choose an operations :")

        second_num = float(input("What is your second number"))
        
        answer =  operations[operation_symbol](first_num,second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")

        choice = input(f"type 'y' to continue to calculating with {answer} or type 'n' to start new calculations ")

        if choice == 'y':
            first_num = answer
        else:
            should_continue = False

        print("\n"*20)
        


calculator()



    