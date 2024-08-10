
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to treasure Island")
print("Your mission is find to treasure")

choice1= input('You\'re at crossroad , where do you want to go ? type "left " or "right".\n').lower()
if choice1 == "left":
    choice2 = input('you\h come to lake. There is island in the middle of lake. Type "wait " for wait a boat or type "swim" to swim to across').lower()
    if choice2 == "wait":
        choice3 = input(' You arrived t the island unharmed. There is house with 3 door one blue one red one yellow. which color do you choose "Blue" "yellow" "red" ').lower()
        if choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "red":
            print("Burned by fired. Game Over.")
        elif choice3 == "yellow":
            print("You win! Congratulations!")
        else:
            print("Game Over.")

    else:
        print("Attached by trout. Game Over")

else :
    print("Fall into a hole, Game Over")
               
