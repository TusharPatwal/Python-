import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("Select 0 for rock, 1 for paper, 2 for scissors :\n"))
if user_choice >= 3 or user_choice < 0:
  print("Invalid number")
else :
  print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You Wins!")
elif user_choice == 0 and computer_choice == 0:
  print("Draw")
elif user_choice == 1 and computer_choice == 0:
  print("You Wins")
elif user_choice == 1 and computer_choice == 1:
  print("Draw")
elif user_choice == 2 and computer_choice == 1:
  print("You Wins")
elif user_choice == 2 and computer_choice == 2:
  print("Draw")
else :
  print("You Lose")
