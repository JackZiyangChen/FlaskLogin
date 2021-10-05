#first file to run in the package
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy() # initialize database
DB_NAME = "database.db"



def create_app():
    app = Flask(__name__) #intialize flask app
    app.config['SECRET_KEY'] = "c3a845a318cd654749ea4db6f4d5f9cb5c6e5b0cade46d9dc04af46d32049c7c" #I love python! 256
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)




    # Register blueprints from views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") # localhost/ will lead to home page
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # SELECT * from User where id=?


    return app


def create_database(app):
    if not path.exists('website'+os.sep+DB_NAME):
        db.create_all(app=app)
        print('database created!')