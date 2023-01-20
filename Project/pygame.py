from random import randint

EASY_LEVEL = 10
HARD_LAVEL = 5

def setDifficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LAVEL

def checkAnswer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns-1
    elif guess < answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}")

def game():
    print("Welcome to the number guessing game!")
    print("Think a number between 1 to 100")
    answer = randint( 1, 100)
    print(f"The correct answer is {answer}")    
    turns = setDifficulty()
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))
        turns = checkAnswer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
      
game()