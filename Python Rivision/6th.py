def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


def square(number):
    return (number*number)

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😒'
    }

    output = ''
    for word in words:
        output += emojis.get(word, words) + ' '
    return output

if __name__ == "__main__":
    # positional argument
    greet_user('Tushar', 'Patwal')
    # keyword argument
    greet_user(last_name='Tripati', first_name='Ansh')

    print(square(55))
    message = input('> ')
    print(emoji_converter(message))