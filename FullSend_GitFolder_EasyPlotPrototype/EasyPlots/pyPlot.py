import plotly.express as px
from jinja2 import Template
from matplotlib import pyplot as plt 
import numpy as np 
import os


def barPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')


def linePlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    fig = plt.figure()
    plt.plot(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')


def dotPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    fig = plt.figure()
    plt.plot(xdata, ydata, 'bo')
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')


def boxPlot(data, plotTitle, xaxisTitle, yaxisTitle):
    
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(float(row[i]))
        restructuredData.append(miniList)
        i += 1

    fig = plt.figure()
    plt.boxplot(restructuredData, patch_artist=True, labels=data[0])
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')


def dotPlot(data, plotTitle, xaxisTitle, yaxisTitle):
    
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(float(row[i]))
        restructuredData.append(miniList)
        i += 1

    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    fig = plt.figure()
    plt.plot(xdata, ydata, 'bo')
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')


def linePlot(data, plotTitle, xaxisTitle, yaxisTitle):

    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(float(row[i]))
        restructuredData.append(miniList)
        i += 1

    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]
    
    fig = plt.figure()
    plt.plot(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')

def barPlot(data, plotTitle, xaxisTitle, yaxisTitle):
    
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(float(row[i]))
        restructuredData.append(miniList)
        i += 1

    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('FullSend_GitFolder_EasyPlotPrototype/EasyPlots/static/pyPlot.png', bbox_inches='tight')