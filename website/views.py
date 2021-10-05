from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db


views = Blueprint('views', __name__) #establish a blueprint for subviews

@views.route('/', methods=['GET','POST'])
# @views.route('/home', methods=['GET', 'POST'])
@login_required
def home(): # redirect user to home page whenever '/' is the input
    if request.method =='POST':
        note = request.form.get("note")
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Successfully added note', category='success')

    return render_template("home.html",user=current_user)