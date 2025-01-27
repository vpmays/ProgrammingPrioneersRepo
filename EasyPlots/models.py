from . import db #from this package import db, which is set to SQLAlchemy()
from flask_login import UserMixin
from sqlalchemy.sql import func


#Table for notes, inherits from db.Model
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    dataString = db.Column(db.String(1000000000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # associate note with user, one to many relationship, id from user

#table for users, inherits from db.Model and UserMixin, need UserMixin because we're using flask_login module
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    #notes = db.relationship('Note') # add note id to list of user notes, allows us to access notes the user created
