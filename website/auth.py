from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db



auth = Blueprint('auth', __name__) #initialize authentication blueprint

@auth.route('/login',methods=['GET','POST'])
def login():  # handles login operation
    data = request.form  # contains form data collected when a post request is generated
    return render_template("login.html")  # NOTE: variable can be passed through method parameter


@auth.route('/logout')
def logout(): #handles logout operation
    return '<p>You have been logged out</p>'


@auth.route('/sign-up', methods=['GET','POST'])
def signup():  # handles sign up operation
    if request.method == 'POST':  # as user clicks on submit button
        # get data from form submitted
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:  # ensure email input is a valid email
            flash('you must have a valid email', category='error')
        elif len(firstName)<2:  # ensure first name is greater than 2 characters
            flash('you must enter a valid first name', category='error')
        elif password1 != password2: # ensure that password confirmation is valid
            flash('Passwords don\'t match', category='error')
        elif len(password1)<7:  # ensure that password is secure enough
            flash('password is too weak. Please try again', category='error')
        elif len(lastName)<2:  # ensure last name is greater than 2 characters
            flash('you must enter a valid last name', category='error')
        else:

            # create new user/add user to database
            new_user = User(email=email, first_name=firstName, last_name=lastName, password=generate_password_hash(password=password1, method='sha256' )) # note: password is hashed through SHA256 algorithm
            db.session.add(new_user)
            db.session.commit()

            # redirect user to home
            flash('successfully created an account', category='success')
            return redirect(url_for('views.home'))



    return render_template("signup.html")
