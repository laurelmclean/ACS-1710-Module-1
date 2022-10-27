# import Flask library

from ast import For
from flask import Flask

# import random

import random

# set up app variable to enable us to write routes

app= Flask(__name__)

# indicates URL of webpage which is homepage
@app.route('/')
def homepage():
    # returns the page contents that will show up in browser
    return 'Are you there, world? It\'s me, Ducky!'


# route for user to add their favourite animal
# URL will be dictated by what animal they select
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    # display message based on user input
    return f'Wow, {users_animal} is my favorite animal, too!'

# Favourite dessert

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    # display message based on user input
    return f'How did you know I liked {users_dessert}?'

# Mad Libs

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    return f'I also love {adjective} {noun}!'

#  Multiply two numbers

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    # validates and multiplies
    if number1.isdigit() and number2.isdigit() == True:
        total = int(number1) * int(number2)
        return f'{number1} times {number2} is {total}!'
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

# say N times


@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    # validates and prints
    if n.isdigit() == True:
        string = (word + ' ')
        return f'{string * int(n)}'
    else:
        return "Invalid input. Please try again by entering a word and a number!"

# dice game

@app.route('/dicegame')
def dice_game():
    roll = random.randint(1, 6)
    # validates and prints
    if roll < 6:
        return f'You rolled a {roll}. You lost!'
    else:
        return f'You rolled a {roll}. You won!'

# tell python how to run the server
# Always needs to be at the very bottom
if __name__ == '__main__':
    app.run(debug=True)
