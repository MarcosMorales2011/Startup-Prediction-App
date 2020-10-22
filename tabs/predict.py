import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash
from joblib import load
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

pipeline = load('model/new_pipeline.joblib')

from app import app

genders = [ 'Male', 
            'Female', 
            'Client refused',     
            'Trans Male (FTM or Female to Male)',
            'Trans Female (MTF or Male to Female)'
            ]

insurances = ['Yes', 
             'No', 
             'Data Not Collected', 
             'Client refused', 
             "Client doesn't know"
             ]            

homeless3years = [
             'One time', 
             'Two times', 
             'Three times',
             'Four or more times',
             'Data not collected',             
             'Client refused',          
             "Client doesn't know"
             ]             

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to predict exit destination of a family based off of features declared by the head of household which proved to have high significance in my prediction model
    
    """), 

    
dbc.Col(
    [

        

        html.H1('Adjust features below to predict the exit destination of household', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),



        dcc.Markdown('## Predictions', className='mb-5'), 

        dcc.Markdown('###### Reported Gender'), 
        dcc.Dropdown(
            id='gender', 
            options=[{'label': purpose, 'value': purpose} for purpose in genders], 
            value=genders[0]
        ), 

        dcc.Markdown('###### Covered by Health Insurance'), 
        dcc.Dropdown(
            id='insurance', 
            options=[{'label': purpose, 'value': purpose} for purpose in insurances], 
            value=insurances[0]
        ), 

        dcc.Markdown('###### How many times homeless in the last 3 years'), 
        dcc.Dropdown(
            id='timeshomeless', 
            options=[{'label': purpose, 'value': purpose} for purpose in homeless3years], 
            value=genders[0]
        ), 
        
        dcc.Markdown('#### Income at Entry'), 
        dcc.Slider(
            id='entry_income', 
            min=0, 
            max=3000, 
            step=100, 
            value=0,
            marks={n: str(n) for n in range(0,3000,100)}, 
            className='mb-5', 
        ), 
        html.Div(id='slider-output-container'),

        dcc.Markdown('#### Length of Time Homeless in days'), 
        dcc.Slider(
            id='length_homeless', 
            min=0, 
            max=400, 
            step=10, 
            value=0,
            marks={n: str(n) for n in range(0,400,10)}, 
            className='mb-5', 
        ), 

        html.Div(id='slider-output-container'),
        
        dcc.Markdown('#### Total HouseHold Size'), 
        dcc.Slider(
            id='CaseMembers', 
            min=1, 
            max=10, 
            step=1, 
            value=1,
            marks={n: str(n) for n in range(1,10,1)}, 
            className='mb-5', 
        ), 

        html.Div(id='slider-output-container'),

        dcc.Markdown('#### Age at Enrollment'), 
        dcc.Slider(
            id='Age_at_Enrollment', 
            min=18, 
            max=65, 
            step=1, 
            value=25,
            marks={n: str(n) for n in range(18,65,1)}, 
            className='mb-5', 
        ), 
        html.Div(id='slider-output-container'),

    ],
    md=4,
)
])
dbc.Col(
    [
        html.H2('Exit To Permanent Housing', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd



@app.callback(
    dash.dependencies.Output('prediction-content', 'children'),
    [dash.dependencies.Input('entry_income', 'value'), dash.dependencies.Input('length_homeless', 'value'), 
    dash.dependencies.Input('CaseMembers', 'value'), dash.dependencies.Input('Age_at_Enrollment', 'value'),
    dash.dependencies.Input('gender', 'value'), dash.dependencies.Input('insurance', 'value'),
    dash.dependencies.Input('timeshomeless', 'value')],
)
def predict(entry_income, length_homeless, CaseMembers, Age_at_Enrollment, gender, insurance, timeshomeless):
    df = pd.DataFrame(
        data=[[np.NaN, np.NaN, 'operation', np.NaN, np.NaN, 'No', np.NaN, 
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN]]
    )
    
    y_pred = pipeline.predict(df)
    
    if y_pred > 0:
        return "Your startup is more likely to succeed."
    else:
        return "Your startup is likely to fail."
