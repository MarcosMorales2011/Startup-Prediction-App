from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

layout = dcc.Markdown("""
## Startup Prediction

What causes a startup to succeed or fail? Startups, or new established businesses, arise commonly in today's economy. In fact, according to SBA estimates, around 627,000 new businesses open each year. But, even if many try to make their own businessess, that does not mean that they are all successful about it. According to investopedia, it is estimated that every eight in ten business end up closing shop within 10 years. 


But what's causing that 20% to find success? This wep application is here to attempt to answer the problem. From a dataset sourced from kaggle.com, over 400 different startups' data was recorded, including features such as their year of funding, their internet activity score, and wether that startup succeeded or failed.  


Using Machine Learning, I'vre created a model that utilizes the startup's information in order to predict if it will fail or succeed. These are the following tabs for the webapp:


Process: Goes into the inner working of the model as well as the data science / machine learning aspect of it


Insights: Showcases a graph of the predicted classifications versus the actual classifications, as well as provide some further visualizations.


Predict: Work with the model directly as you input the required features, and get back the probability of your startup succeeding!
""")