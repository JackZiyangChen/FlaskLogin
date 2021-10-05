from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__) #initialize authentication blueprint

@auth.route('/login',methods=['GET','POST'])
def login():  # handles login operation
    data = request.form  # contains form data collected when a post request is generated
    if request.method == 'POST':
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first() # SELECT * from User where email like ?
        if user:
            if check_password_hash(user.password,password):
                flash('Login successfully!',category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Password Incorrect!',category='error')
        else:
            flash('user does not exist!',category='error')

    return render_template("login.html", user=current_user)  # NOTE: variable can be passed through method parameter


@auth.route('/logout')
@login_required
def logout(): # handles logout operation
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def signup():  # handles sign up operation
    if request.method == 'POST':  # as user clicks on submit button
        # get data from form submitted
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if len(email)<4:  # ensure email input is a valid email
            flash('you must have a valid email', category='error')
        elif user:
            flash('User already exist!', category='error')
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
            login_user(new_user,remember=True)

            # redirect user to home
            flash('successfully created an account', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)
