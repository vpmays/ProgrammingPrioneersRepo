from flask import Blueprint, render_template, request, flash, jsonify #import needed modules from flask
from flask_login import login_required, current_user #anything on the user table can be accessed with current_user
from .models import Note
from . import db
import json
from .pyPlot import pyPlot1, pyPlot2

views = Blueprint('views', __name__) # intialize Blueprint("nmae of blueprint", __name__) and store it as "views" object

# @ is how you define a view/route. format is @nameOfBlueprint.route("url to get to this endpoint", methods = [the methods you will alow])
@views.route('/', methods=['GET', 'POST']) #defining homepage so route is just '/', and we need to allow GET and POST methods on this page
@login_required #require the user to be logged in to get to this page
#this function will run when we go into our home (index page) of our webapp
def home(): #when you hit route '/' (homepage) this function is called
    #if method is 'POST' when you hit the home page, get the note and check it, then store it in db
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note must be at least 1 character.', category='error' )
        else:
            new_note = Note(data=note, user_id=current_user.id)
            #store note in db
            db.session.add(new_note)
            db.session.commit()
            #notify user that note was stored
            flash('Note added!', category='success')
            #using date from note to plug into pyPlots. This is where we will pull in data from template plot form
            pyPlot1(note)
            pyPlot2(note)
            #render/display the html page home.html with user set to current_user, 
            #   must be in folder named templates to find it with this function,
            #   can add any variables we want (in this case we created a 'user' variable) which we can then access in the 
            #   hmtl file.
    return render_template("home.html", user=current_user)

#route for deleting notes. I'm thinking we won't need this for our code
@views.route('/delete-note', methods=['POST'])
def delete_note():
    #json.load() takes your jason string and turns it into a python dictionary object
    note = json.loads(request.data)
    #pull noteId form diction and save as noteId variable
    noteId = note['noteId']
    # query Note table and use get() the accesses the note with primary key == noteId
    note = Note.query.get(noteId)
    #if ntoe exists and it's userId matches the current userId, delete it
    if note:
        if note.user_id == current_user.id:
            #delete note from db
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({}) #just return an empty response because flask requires us to return something 

@views.route('/pyPlot')
def pyPlot():
    return render_template("pyPlot.html") #render/display the html page pyPlot.html, must be in folder named templates to find it with this function