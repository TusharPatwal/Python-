# number guessing game
import random
from pygame02_art import logo
EASY = 10
MEDIUM = 7
HARD = 5

def check(answer, guess, turns):
    if answer > guess:
        print("Too Low.")
        return turns-1
    elif answer < guess:
        print("Too High.")
        return turns-1
    else:
        print("You got the answer!")
        
def setDifficulty():     
    level = input("enter 'easy', 'medium' or 'hard': ")
    if level == 'easy':
        return EASY
    elif level == 'medium':
        return MEDIUM
    else:
        return HARD
    
    
def game():
    print(logo)
    print("Welcome to the number guessing game!")
    answer = random.randint(1, 100)
    print(f"The answer is {answer}")
    turns = setDifficulty()
    guess = 0        
    while answer != guess:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("enter the guessed number: "))
    
        turns = check(answer, guess, turns)
        if turns == 0:
            print("You are out of guesses")
            return
        elif guess != answer:
            print("Try again")

game()