import plotly.express as px
from jinja2 import Template
from matplotlib import pyplot as plt 
from scipy.stats import linregress, wilcoxon, ttest_ind
import numpy as np 
import os


def barPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')


def linePlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle):
    
    fig = plt.figure()
    plt.plot(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')


def dotPlot1(xdata, ydata, plotTitle, xaxisTitle, yaxisTitle, stats):

    linearRegress = False
    fig = plt.figure()
    plt.plot(xdata, ydata, 'o')
    if stats == "linearRegress":
        print(xdata)
        print(ydata)
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

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')
    return linearRegress


def boxPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):
    
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)
        print(tTestSelection1)
        print(tTestSelection2)
        

    fig = plt.figure()
    plt.boxplot(restructuredData, patch_artist=True, labels=data[0])
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')
    return [test, stats]


def dotPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):
    
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)

    fig = plt.figure()
    plt.plot(xdata, ydata, 'bo')
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')
    return [test, stats]


def linePlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):

    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)

    fig = plt.figure()
    plt.plot(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')
    return [test, stats]

def barPlot(data, tTestSelection1, tTestSelection2, plotTitle, xaxisTitle, yaxisTitle, stats):
    
    restructuredData = []

    i = 0
    for elem in range(len(data[0])):
        miniList = []
        for row in data[1:]:
            miniList.append(row[i])
        restructuredData.append(miniList)
        i += 1

    ydata = []
    for variable in restructuredData:
        ydata.append(sum(variable)/len(variable))
    
    xdata = data[0]

    test = False
    if stats == "tTest":
        test = ttest_ind(tTestSelection1,tTestSelection2)
    elif stats == "wilcoxon":
        test = wilcoxon(tTestSelection1,tTestSelection2)
    
    fig = plt.figure()
    plt.bar(xdata, ydata)
    plt.xticks(rotation = 45)
    plt.xlabel(xaxisTitle)
    plt.ylabel(yaxisTitle)
    plt.title(plotTitle)

    fig.savefig('EasyPlots/static/pyPlot.png', bbox_inches='tight')
    return [test, stats]