from . import db # importing from current package
from flask_login import UserMixin
from sqlalchemy.sql import func

# each class represents a table in the database

class Note(db.Model): # Create a Note table
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # establish a foreign key to authenticate user id
    # NOTE: A foreign key that connects to a column from another table
    # used to denote one to many relationships



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')
