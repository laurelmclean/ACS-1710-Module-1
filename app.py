# import Flask library

from flask import Flask

# set up app variable to enable us to write routes

app= Flask(__name__)

# indicates URL of webpage which is homepage
@app.route('/')
def homepage():
    # returns the page contents that will show up in browser
    return 'Are you there, world? It\'s me Ducky!'

# tell python how to run the server
if __name__ == '__main__':
    app.run(debug=True)