import plotly.express as px
from jinja2 import Template
from matplotlib import pyplot as plt 
from scipy.stats import linregress, wilcoxon, ttest_ind
import numpy as np 
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()

def barPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    #build plot
    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')


def linePlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    #check to see if x-data is numeric
    xdataIsNumerical = True
    xdata_ = []
    i = 0
    for val in xdata: 
        try:
            xdata_.append(float(val))
        except:
            xdataIsNumerical = False
        i += 0

    if (xdataIsNumerical):
        xdata = xdata_

    #build plot
    fig = plt.figure()
    plt.plot(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')


def dotPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle, stats):

    #check to see if x-data is numeric
    xdataIsNumerical = True
    xdata_ = []
    i = 0
    for val in xdata: 
        try:
            xdata_.append(float(val))
        except:
            xdataIsNumerical = False
        i += 0

    if (xdataIsNumerical):
        xdata = xdata_

    #create linear regression variable
    linearRegress = False

    #build plot and include linear regression if needed
    fig = plt.figure()
    plt.plot(xdata, ydata, 'o')
    if stats == "linearRegress":
        linearRegress = linregress(xdata,ydata)
        m, b = np.polyfit(xdata, ydata, 1)
        newYdata = []
        for xval in xdata:
            newYdata.append(m*xval+b)
        plt.plot(xdata, newYdata, linewidth=2)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')
    return linearRegress


def boxPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):
    
    #create new list to store restuctured data
    restructuredData = []

    #restructure data
    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    #perform statistical test
    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)
        
    #build plot
    fig = plt.figure()
    plt.boxplot(restructuredData, patch_artist=True, labels=data[0])
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')
    return [test, stats]


def dotPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):

    #restructure data
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    #get mean
    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    #check to see if x-data is numeric
    xdataIsNumerical = True
    xdata_ = []
    i = 0
    for val in xdata: 
        try:
            xdata_.append(float(val))
        except:
            xdataIsNumerical = False
        i += 0

    if (xdataIsNumerical):
        xdata = xdata_

    #perform statistical test
    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)

    #build plot
    fig = plt.figure()
    plt.plot(xdata, ydata, 'bo')
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')
    return [test, stats]


def linePlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):

    #restructure data
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    #get mean
    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    #check to see if x-data is numeric
    xdataIsNumerical = True
    xdata_ = []
    i = 0
    for val in xdata: 
        try:
            xdata_.append(float(val))
        except:
            xdataIsNumerical = False
        i += 0

    if (xdataIsNumerical):
        xdata = xdata_

    #perform statistical test
    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)

    #build plot
    fig = plt.figure()
    plt.plot(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')
    return [test, stats]

def barPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):
    
    #restructure data
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    #get mean
    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    #perform statistical test
    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)
    
    #build plot
    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig(THIS_FOLDER / 'static/pyPlot.png', bbox_inches='tight')
    return [test, stats]