from flask import Blueprint, render_template, request, flash, redirect, url_for #import needed modules from flask
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user #allows us to easily handle user login tasks


auth = Blueprint('auth', __name__) #auth blueprint for navigating authentication pages

@auth.route("/login", methods=['GET', 'POST']) #this is the route for the '/login' endpoint (our login page), 'GET' and 'POST' methods are allowed
def login():
    # 'request' was imported from flask and has methods to allows us to work with html form
    # set condition to check if 'POST' request was used on the web page
    #   if so, pull information and store as python variables
    if request.method == 'POST':
        # ger user credentials
        email = request.form.get('email')
        password = request.form.get('password')
        
        # query the USer database and look for users data in database
        user = User.query.filter_by(email=email).first() #filter all of the emails with this specific email (grab the first one)
        #if user exists, chekc password
        if user:
            #check password by hashing the user.passowrd and the password the user provided and seeing if they match
            if check_password_hash(user.password, password):
                #if the passwords match, password is correct so login user and flash message of succewssful login
                flash('Login successful!', category='success')
                #login user
                login_user(user, remember=True)
                #redirect user to home page
                return redirect(url_for('views.upload'))
            # if incorrect password, flash message to user
            else:
                flash('Incorrect password. Please try again.', category='error')
        #if email does not exist, flash message to user
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user) #render/display the login.html page,must be in folder named templates to find it with this function

@auth.route('/logout') #this is the route for the '/logout' endpoint (our logout page), no methods are allowed
@login_required #means you must be logged in to be able to access this page
def logout():
    #logout current user
    logout_user()
    return redirect(url_for('auth.login')) #redirect ot auth.login, which starts you back at @auth.route("/login", methods=['GET', 'POST'])

@auth.route("/sign_up", methods=['GET', 'POST']) #this is the route for the '/sign_up' endpoint (our sign up page), 'GET' and 'POST' methods are allowed
def signUp():
    # check if form was submitted by checking if post method was used on web page
    if request.method=='POST':
        # set python variables from form if so
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # check if user in database already and all the requirements for email, passwaord, etc., are met
        #   flash a message with error if there is an issue
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(username) < 1:
            flash('Username must be at least 1 character long.', category='error')
        elif len(email) < 6:
            flash('Email must be at least 6 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        else:
            # create user if all tests pass
            # use User class in 'models.py'
            new_user = User(username=username, email=email, 
                            password=generate_password_hash(password1, method='pbkdf2')) # we use hash function on the password to secure it
            # add the user to database and update the database
            db.session.add(new_user)
            db.session.commit()
            # once user is cerate, login the user, remember the user is logged in, and relay login message to user
            login_user(new_user, remember=True)
            flash('Your account has been created!', category='success')
            return redirect(url_for('views.upload')) #redirect ot views.home, which starts you back at @views.route('/', methods=['GET', 'POST']) and has the function name 'home'

    return render_template("sign_up.html", user=current_user) #render/display the sign_up.html page, must be in folder named templates to find it with this function