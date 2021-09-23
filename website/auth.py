from flask import Blueprint, render_template


auth = Blueprint('auth', __name__) #initialize authentication blueprint

@auth.route('/login')
def login(): #handles login operation
    return render_template("login.html") #NOTE: variable can be passed through method parameter


@auth.route('/logout')
def logout(): #handles logout operation
    return '<p>You have been logged out</p>'


@auth.route('/sign-up')
def signup(): #handles sign up operation
    return render_template("signup.html")
