
from flask import Flask, render_template, redirect, url_for, request
import os

# create the application object
app = Flask(__name__)

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
        
    if error == None:
        return render_template('/login.html', error=error), 200
    else:
        return render_template('/login.html', error=error), 401

    # Route for handling the login page logic
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('/home.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)