import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

import os
import sys
import copy

from src.graphs import dist_tenure, dist_monthlycharges, dist_totalcharges

#-------------------------------------------------------------------------------
# DATA ANALYSIS
#-------------------------------------------------------------------------------

# Tenure Distribution

card_tensure = dbc.Card(
    dbc.CardBody(
        dcc.Graph(figure = dist_tenure(), config = {"displayModeBar": False}, style = {"height": "42vh"})
    ),
    style = {"background-color": "#16103a"}
)

# Monthly Charges Distribution

card_monthlycharges = dbc.Card(
    dbc.CardBody(
        dcc.Graph(figure = dist_monthlycharges(), config = {"displayModeBar": False}, style = {"height": "42vh"})          
    ),
    style = {"background-color": "#16103a"}
)

# Total Charges Distribution

card_totalcharges = dbc.Card(
    dbc.CardBody(
        dcc.Graph(figure = dist_totalcharges(), config = {"displayModeBar": False}, style = {"height": "42vh"})
    ),
    style = {"background-color": "#16103a"}
)

# Categorical Bar Chart

card_categorical = dbc.Card(
    dbc.CardBody(
        dbc.Spinner(
            size="md",
            color="light",
            children=[
                dcc.Graph(id="categorical_bar_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
            ]
        ),
        style = {"height": "52vh"}
    ),
    style = {"background-color": "#16103a"}
)

# Donut Chart

card_donut = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_pie_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ], style = {"height": "52vh"}
        ),
    ],
    style = {"background-color": "#16103a"}
)

# TABS

tab_graphs = [

    # Categorical Fetaures Visualization
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [

                            dbc.Col([
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon("Categorical Feature", addon_type="prepend"),
                                        dbc.Select(
                                            options=[
                                                {"label": "Gender", "value": "gender"},
                                                {"label": "Partner", "value": "Partner"},
                                                {"label": "Dependents", "value": "Dependents"},
                                                {"label": "Phone Service", "value": "PhoneService"},
                                                {"label": "Multiple Lines", "value": "MultipleLines"},
                                                {"label": "Internet Service", "value": "InternetService"},
                                                {"label": "Online Security", "value": "OnlineSecurity"},
                                                {"label": "Online Backup", "value": "OnlineBackup"},
                                                {"label": "Device Protection", "value": "DeviceProtection"},
                                                {"label": "Tech Support", "value": "TechSupport"},
                                                {"label": "Streaming TV", "value": "StreamingTV"},
                                                {"label": "Streaming Movies", "value": "StreamingMovies"},
                                                {"label": "Contract", "value": "Contract"},
                                                {"label": "Paperless Billing", "value": "PaperlessBilling"},
                                                {"label": "Payment Method", "value": "PaymentMethod"},
                                                {"label": "Senior Citizen", "value": "SeniorCitizen"},
                            
                                            ], id = "categorical_dropdown", value="gender"
                                        )
                                    ]
                                ),


                                html.Img(src="../assets/customer_churn.jpg", className="customer-img")
                                
                                
                                ],lg="4", sm=12,
                            ),


                            dbc.Col(card_donut, lg="4", sm=12),
                            dbc.Col(card_categorical, lg="4", sm=12),

                        ], className="h-15", style={"height": "100%"}
                    )
                ]
            ),
            className="mt-3", style = {"background-color": "#272953"}
        ),

    # Tensure, MonthlyCharges and TotalCharges Visualizaion

    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(card_tensure, lg="4", sm=12),
                        dbc.Col(card_monthlycharges, lg="4", sm=12),
                        dbc.Col(card_totalcharges, lg="4", sm=12),  
                    ], className="h-15"
                )
            ]
        ),
        className="mt-3", style = {"background-color": "#272953"}
    )

]

tab_analysis_content = tab_graphs
