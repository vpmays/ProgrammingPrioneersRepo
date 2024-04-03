from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() #create database
DB_NAME = "database.db" #set db name

def create_app():
    app = Flask(__name__) #make app opject, initialize app
    app.config['SECRET_KEY'] = 'fgboasefkjbw dfkjsafkjb' #set security key for website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #tell application where database is
    db.init_app(app) #initialize database by giving it our flask app

    from .views import views #import views from views.py file, our blueprint in this file was named views
    from .auth import auth #import auth from auth.py file, our blueprint in this file was named auth

    #tell the application where our blueprints are
    app.register_blueprint(views, url_prefix='/') #register the blueprint, the prefix of '/' just means no prefix video 18:26
    app.register_blueprint(auth, url_prefix='/') #register the blueprint, the prefix of '/' just means no prefix video 18:26

    from .models import User, Note # import our two database tables, we don't actually use them but having this defines them before creating our db

    create_database(app)
    
    #
    login_manager = LoginManager()
    #redirect user to login page if user is not logged in
    login_manager.login_view = 'auth.login'
    #tells the lofin manager where the app is
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #when we use get() it knows to look for primary key you give it

    return app #return application

#only creates db if the db doesn't exist
def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')