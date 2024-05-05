'''import create_app function from __iti__.py file, we use the 
 EasyPlots folder name because __init__.py runs automatically 
 when we import EasyPlots folder'''
from EasyPlots import create_app 
app = create_app() #set creat_app() function to variable app

if __name__ == '__main__': #makes it where you only run the webserver if you run this file
    #this runs the application and web server, debug=true means when we make a change it wll 
    # automatically rerun the web server. Will turn tis off when we run in production.
    app.run(debug=True) 