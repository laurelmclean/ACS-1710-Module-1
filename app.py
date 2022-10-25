# import Flask library

from flask import Flask

# set up app variable to enable us to write routes

app= Flask(__name__)

# indicates URL of webpage which is homepage
@app.route('/')
def homepage():
    # returns the page contents that will show up in browser
    return 'Are you there, world? It\'s me Ducky!'


# route for user to add their favourite animal
# URL will be dictated by what animal they select
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    # display message based on user input
    return f'Wow, {users_animal} is my favorite animal, too!'


# tell python how to run the server
# Always needs to be at the very bottom
if __name__ == '__main__':
    app.run(debug=True)
