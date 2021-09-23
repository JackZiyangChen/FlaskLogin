from flask import Blueprint, render_template


views = Blueprint('views', __name__) #establish a blueprint for subviews

@views.route('/')
@views.route('/home') #decorator
def home(): #redirect user to home page whenever '/' is the input
    return render_template("home.html")