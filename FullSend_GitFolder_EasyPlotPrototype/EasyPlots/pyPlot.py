import plotly.express as px
from jinja2 import Template
from matplotlib import pyplot as plt 
import numpy as np 


def pyPlot1(freq=1):
    t = np.arange(0.0, 2.0, 0.1)
    s = 1 + np.sin(float(freq)*np.pi*t)

    fig, ax = plt.subplots()
    ax.plot(t,s)
    ax.set(xlabel="time (s)", ylabel="voltage (mV)",
            title='Made with matplotlib')
    ax.grid()

    fig.savefig('EasyPlots/static/pyPlot.png')


def pyPlot2(value=1):
    '''
    [8,4,3,2,1,1]
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')

    output_html_path=r"EasyPlots/templates/pyPlot.html"
    input_template_path = r"EasyPlots/templates/home.html"

    plotly_jinja_data = {"fig":fig.to_html(full_html=False)}
    #consider also defining the include_plotlyjs parameter to point to an external Plotly.js as described above

    with open(output_html_path, "w", encoding="utf-8") as output_file:
        with open(input_template_path) as template_file:
            j2_template = Template(template_file.read())
            output_file.write(j2_template.render(plotly_jinja_data))
    '''
    experience_dict = {'Programming Language': ['Excel', 'Python', 'Tableau', 'R', 'Bash', 'PowerShell'], 'Years of Experience (As of April 2022)': [float(value),4,3,2,1,1]}

    fig = px.bar(experience_dict, x='Programming Language', y='Years of Experience (As of April 2022)')

    fig.write_html("EasyPlots/templates/pyPlot.html")

