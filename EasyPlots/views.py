from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for #import needed modules from flask
from flask_login import login_required, current_user #anything on the user table can be accessed with current_user
# from .models import Note
from . import db
import json
from .pyPlot import barPlot1, boxPlot, linePlot1, dotPlot1, barPlot, linePlot, dotPlot # , pyPlot2
import os
from .models import User
from .models import UserData
import csv
from pathlib import Path

views = Blueprint('views', __name__) # intialize Blueprint("nmae of blueprint", __name__) and store it as "views" object
plotTitle = '' #put this out here so I could access it in the pyPlot route
data = []
THIS_FOLDER = Path(__file__).parent.resolve()


# @ is how you define a view/route. format is @nameOfBlueprint.route("url to get to this endpoint", methods = [the methods you will alow])
@views.route('/', methods=['GET', 'POST']) #defining homepage so route is just '/', and we need to allow GET and POST methods on this page
@login_required #require the user to be logged in to get to this page
#this function will run when we go into our home (index page) of our webapp
def home(): #when you hit route '/' (homepage) this function is called
    isPostRequest = False
    #if method is 'POST' when you hit the home page, get the note and check it, then store it in db
    if request.method == 'POST':
        isPostRequest = True

        #get data from html form
        dataStructure = request.form.get('dataStructure')
        plotType = request.form.get('plotType')
        xdata_index = int(request.form.get('xdata1')) #data comes back as string for now, so need ot 
        ydata_index = int(request.form.get('ydata1')) #data comes back as string for now, so need ot 
        
        plotTitle = request.form.get('plotTitle')
        xaxisTitle = request.form.get('xaxisTitle')
        yaxisTitle = request.form.get('yaxisTitle')

        stats = request.form.get('stats')
        tTestSelection1_index = int(request.form.get('tTestSelection1'))
        tTestSelection2_index = int(request.form.get('tTestSelection2'))

        #make x and y data
        # set up data based on structure and statistics choices
        xdata = []
        ydata = []
        if (dataStructure == 'oneXOneY' and stats == 'linearRegress'):
            i = 0
            for row in data[1:]:
                try:
                    xdata.append(float(row[xdata_index]))
                    ydata.append(float(row[ydata_index]))
                except:
                    flash('For linear regression x and y values must be real numbers.', category='error')
                    buildPlot = False
                    return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
                i += 1
            if i < 2:
                flash('You must have at least two values for each variable in linear regression.', category='error')
                buildPlot = False
                return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
        elif (dataStructure == 'oneXOneY' and stats != 'linearRegress'):
            for row in data[1:]:
                xdata.append(row[xdata_index])
                try:
                    ydata.append(float(row[ydata_index]))
                except:
                    flash('y values must be real numbers.', category='error')
                    buildPlot = False
                    return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
        else:
            i = 1
            for row in data[1:]:
                j = 0
                for elem in row:
                    try:
                        data[i][j] = float(elem)
                    except:
                        flash('All variable values in your dataset must be real numbers.', category='error')
                        buildPlot = False
                        return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
                    j += 1
                i += 1

        #do additional checks needed for ttest and wilcoxon test
        if (tTestSelection2_index == tTestSelection1_index) and (stats == "wilcoxon" or stats == "tTest"):
            flash('You must compare two different variables.', category='error')
            buildPlot = False
            return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
        
        #build ttest and wilcoxon test variables, make needed check along the way
        tTestSelection1 = []
        tTestSelection2 = []
        for row in data[1:]:
            if (stats == "wilcoxon" or stats == "tTest"):
                try:
                    tTestSelection1.append(float(row[tTestSelection1_index]))
                    tTestSelection2.append(float(row[tTestSelection2_index]))
                except:
                    flash('Variables for stats tests must be real numbers.', category='error')
                    buildPlot = False
                    return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
        
        #check if dotPlot was chosen when doing linear regression
        if (stats == 'linearRegress'):
            if (plotType != "dotPlot"):
                flash('You must use dot plot for linear regression.', category='error')
                buildPlot = False
                return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
        elif (stats != 'noStats'):
            if (dataStructure != 'oneXManyY'):
                flash('You must have multiple numeric y values for each x variable to perform ttest or wilcoxon test.', category='error')
                buildPlot = False
                return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)

        
        #set up linear regression and ttest variables then call proper statistics functions
        linearRegression = False
        tTest = False
        if dataStructure == 'oneXOneY':
            if plotType == 'barPlot':
                barPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle)
            elif plotType == 'linePlot':
                linePlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle)
            elif plotType == 'dotPlot':
                linearRegression = dotPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle, stats)
            elif plotType == 'boxPlot':
                flash('The structure of your data must be "Each x variable has more than one y value.', category='error')
                buildPlot = False
                return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)
        else:
            if plotType == 'boxPlot':
                tTest = boxPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats)
            elif plotType == 'barPlot':
                tTest = barPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats)
            elif plotType == 'linePlot':
                tTest = linePlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats)
            elif plotType == 'dotPlot':
                tTest = dotPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats)

        #load html based on post method, will build plot with form data
        buildPlot = True
        return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot, linearRegression=linearRegression, tTest=tTest)
    #load htmkl based on a request method, no plot should apper on page
    buildPlot = False
    return render_template("home.html", user=current_user, userData=data, isPostRequest=isPostRequest, buildPlot=buildPlot)

@views.route('/upload', methods=['GET', 'POST']) #defining upload page with route '/upload', we need to allow GET and POST methods on this page
@login_required #require the user to be logged in to get to this page
def upload():
    
    #check if it's get or post request
    if request.method == 'POST':
        #capture uploaded csv
        uploaded_csv = request.files['file']
        #check if a csv was submitted
        if uploaded_csv.filename != '':
            if ((len(uploaded_csv.filename) < 5) or (uploaded_csv.filename[-4:] != '.csv')):
                flash('File type must be .csv and file name must be at least 1 character long.', category='error')
                return render_template("upload.html", user=current_user)
            uploaded_csv.save(THIS_FOLDER / uploaded_csv.filename)
            basename = uploaded_csv.filename[:-4]

            #get data from uploaded csv then delete csv
            dataString = ""
            with open(THIS_FOLDER / uploaded_csv.filename) as csvfile:
                reader = csv.reader(csvfile)
                newReader = []
                for row in reader:
                    newReader.append("EasyPlotElementJoiner".join(row))
                dataString = "EasyPlotLineJoiner".join(newReader)
            os.remove(THIS_FOLDER / uploaded_csv.filename)
            dataName = UserData.query.filter_by(user_id=current_user.id, title=basename).first()
            if dataName:
                #check if filenam already in db for user
                flash('File name already exists.', category='error')
            else:
                #add user data to UserData table
                newData = UserData(title=basename, dataString=dataString, 
                            user_id=current_user.id) # we use hash function on the password to secure it
                # add the user to database and update the database
                db.session.add(newData)
                db.session.commit()
            
            return redirect(url_for('views.plotTemplate', user=current_user))
    
    return render_template("upload.html", user=current_user)

@views.route('/plotTemplate', methods=['GET', 'POST'])
@login_required #require the user to be logged in to get to this page
def plotTemplate():
    #print(data)
    if request.method == 'POST':
        selectedData = request.form.get('dataString').split()
        selectedData[0] = selectedData[0][1:-1]
        selectedData[1] = selectedData[1][1:-2]
        #print(selectedData)
        useOrDelete = request.form.get('useOrDelete')
        if useOrDelete == "useData":
            #clear the data list but don't create data variable
            for num in range(len(data)):
                data.pop(0)
            userData = selectedData[1].split('EasyPlotLineJoiner')
            #print(data)
            #i = 0
            #replensih data list with new data
            for row in userData:
                #print(row)
                data.append(row.strip().split('EasyPlotElementJoiner'))
                #i += 1
            #print(data)
            return redirect(url_for("views.home", user=current_user))
        elif useOrDelete == "deleteData":
            datasetToDelete = UserData.query.get(int(selectedData[0]))
            db.session.delete(datasetToDelete)
            db.session.commit()
    allUserData = UserData.query.filter_by(user_id=current_user.id).all()
    return render_template("plotTemplate.html", user=current_user, allUserData=allUserData)