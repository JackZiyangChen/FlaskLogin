from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__) #establish a blueprint for subviews

@views.route('/')
@views.route('/home') # decorator
@login_required
def home(): #redirect user to home page whenever '/' is the input
    return render_template("home.html")