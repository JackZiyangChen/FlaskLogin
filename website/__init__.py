#first file to run in the package
from flask import Flask


def create_app():
    app = Flask(__name__) #intialize flask app
    app.config['SECRET_KEY'] = "c3a845a318cd654749ea4db6f4d5f9cb5c6e5b0cade46d9dc04af46d32049c7c" #I love python! 256

    # Register blueprints from views and auth
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") # localhost/ will lead to home page
    app.register_blueprint(auth, url_prefix="/")

    return app