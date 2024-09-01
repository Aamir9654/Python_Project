import random
from  random import randint

print("Welcome to number gussing name ")
print("thinking number between 1 to 100 ")

print(random.randint(1,100))
answer  = random.randint(1,100)
EASY_LEVEL_TURN =10
HARD_LEVEL_TURN = 5
#function to check user guess and actual guess
def game():
    def check_answer(user_guess, actual_guess,turn):
        if user_guess < actual_guess:
                print("To low !")
                return turn -1
        
        elif user_guess > actual_guess:
                print("To High")
                return turn -1
        else:
                print(f"You got it right the answer was {actual_guess}")

            
    def set_difficulty():
        level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
        if level == "easy":
                return EASY_LEVEL_TURN
        else:
                return HARD_LEVEL_TURN
            


    turn = set_difficulty()
    
    


        
    guess =0
    while guess!=answer:

        guess = int(input("Guess the numbers : "))
        print(f"You have {turn} guesses remaining")

        if(turn == 0):
              print(f"You have run out of guesses, the number was {answer}")
              break

        turn = check_answer(guess,answer,turn)
        
     
    
game()
    