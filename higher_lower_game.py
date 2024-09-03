import random

# data 
indian_celebrities = [
    {
        "name": "Virat Kohli",
        "follower_count": 260000000,
        "description": "Carpediem!",
        "country": "India"
    },
    {
        "name": "Priyanka Chopra",
        "follower_count": 90000000,
        "description": "Actor, Producer, UNICEF Goodwill Ambassador",
        "country": "India"
    },
    {
        "name": "Alia Bhatt",
        "follower_count": 81000000,
        "description": "Moody, Floaty, Fire and Desire. ☁️",
        "country": "India"
    },
    {
        "name": "Shraddha Kapoor",
        "follower_count": 83000000,
        "description": "Actress | UNDP Goodwill Ambassador",
        "country": "India"
    },
    {
        "name": "Ranveer Singh",
        "follower_count": 44000000,
        "description": "Living the dream!",
        "country": "India"
    }
]
#generate a random account from each data
score = 0



# format account into printable format
def format_data(account):
    account_name = account["name"]
   
    account_description = account["description"]
    account_country = account["country"]


    return f"{account_name},{account_description}, from {account_country}"
 # "Take a user guess and the followers count and return if they got it right !"
def check_answer(user_guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"

game_should_contuine = True

while game_should_contuine:

    account_a= random.choice(indian_celebrities)
    account_b= random.choice(indian_celebrities)



    if account_a == account_b:
        account_b = random.choice(indian_celebrities)

    print(f" Compare A : {format_data(account_a)}")
    logo = '''
____   _____________
\   \ /   /   _____/
 \   Y   /\_____  \ 
  \     / /        
   \___/ /_______  /
                 \/ 
                 
                 '''
    print(logo)
    print(f" Compare B : {format_data(account_b)}")

    #ask users for guess

    guess = input("who has more followers? Type 'A' or 'B' ").lower()

    #check if user is correct
    #get follower count for each account
    a_follower_count = account_a["follower_count"]

    b_follower_count =  account_b["follower_count"]


    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # give user feedback on therir name
    if is_correct:
        score = score +1
        print(f"You're right! current_score : {score}")
    else:
        print(f"Sorry, that's wrong! final score : {score}")
        game_should_contuine = False

