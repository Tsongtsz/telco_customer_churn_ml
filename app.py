"""
Telco Customer Churn Analysis
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import no_update

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

import os
import sys
import copy
import time

from src.graphs import df, layout
from content import tab_analysis_content

# Creating the app

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets = [dbc.themes.SUPERHERO,'/assets/styles.css']
)

server=app.server

# Tabs Content

tabs = dbc.Tabs(
    [
        dbc.Tab(tab_analysis_content, label="Data Analysis"),
    ]
)

# Jumbotron

jumbotron = dbc.Jumbotron(
    html.H4("Telco Customer Churn Analysis"),
    className="cover"
)

#-------------------------------------------------------------------------------
# APPLICATION LAYOUT
#-------------------------------------------------------------------------------

app.layout = html.Div(
    [
        jumbotron,
        html.Div(
            dbc.Row(dbc.Col(tabs, width=12)),
            id="mainContainer",
            style={"display": "flex", "flex-direction": "column"}
        )
    ],
)

#-------------------------------------------------------------------------------
# CALLBACKS
#-------------------------------------------------------------------------------

# Data Analysis Tab - Categorical Bar Chart 

@app.callback(
    Output("categorical_bar_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def bar_categorical(feature):

    time.sleep(0.2)

    temp = df.groupby([feature, 'Churn']).count()['customerID'].reset_index()
    
    fig = px.bar(temp, x=feature, y="customerID",
             color=temp['Churn'].map({'Yes': 'Churn', 'No': 'NoChurn'}),
             color_discrete_map={"Churn": "#47acb1", "NoChurn": "#f26522"},
             barmode='group')
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Distribution by Churn"
    
    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        #xaxis_visible=False,
        xaxis_title="",
        yaxis_title="Count",
        legend_title_text="",
        legend = {'x': 0.16}
    )
    return fig

@app.callback(
    Output("categorical_pie_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

# Data Analysis Tab - Donut Chart 

def donut_categorical(feature):

    time.sleep(0.2)

    temp = df.groupby([feature]).count()['customerID'].reset_index()

    fig = px.pie(temp, values="customerID", names=feature, hole=.5)

    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Percentage"

    if(df[feature].nunique() == 2):
        _x = 0.3
    elif(df[feature].nunique() == 3):
        _x = 0.16
    else:
        _x = 0

    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        legend = {'x': _x}
    )

    return fig


#-------------------------------------------------------------------------------
# MAIN FUNCTION
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)