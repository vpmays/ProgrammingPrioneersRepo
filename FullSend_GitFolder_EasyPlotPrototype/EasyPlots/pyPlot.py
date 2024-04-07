import plotly.express as px
from jinja2 import Template
from matplotlib import pyplot as plt 
import numpy as np 


def pyPlot1(xdata=None, ydata=None, plotTitle='Main', xaxisTitle='x-axis', yaxisTitle='y-axis'):
    if xdata == None:
        xdata = ['default', 'defaul', 'default']
    if ydata == None:
        ydata = [3,2,1]
    
    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)
    
    fig.savefig('EasyPlots/static/pyPlot.png')


def pyPlot2(xdata=None, ydata=None, plotTitle='Main', xaxisTitle='x-axis', yaxisTitle='y-axis'):
    
    if xdata == None:
        xdata = ['default', 'defaul', 'default']
    if ydata == None:
        ydata = [3,2,1]
    
    experience_dict = {}
    experience_dict[xaxisTitle] = xdata
    experience_dict[yaxisTitle] = ydata
    
    fig = px.bar(experience_dict, x=xaxisTitle, y=yaxisTitle, title=plotTitle)

    fig.write_html("EasyPlots/templates/pyPlot.html")

