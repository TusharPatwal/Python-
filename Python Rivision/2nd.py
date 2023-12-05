# # guessing game
#
# serect_number = int(input('Enter the number: '))
# guess_count = 0
# guess_limit = 4
#
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == serect_number:
#         print("You Won!")
#         break
# else:
#     print("You Fail!")

command = ''
started = False
while command != 'quit':
    command = input('> ').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
 to exit
        ''')
    elif command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            print('Car stopped...')
    else:
        print("Sorry, I don't understand that!")
