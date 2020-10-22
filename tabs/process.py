from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
layout = [dcc.Markdown("""
### Process

Although we already had a dataset we could work on, that is not enough for us to formulate a machine learning model. First, we have to do an essential aspect, data cleaning.

First, as we loaded the dataset into a dataframe, we had to understand our target, or the variable we would try to predict. After taking a look at all the features, there was a perfect candidate. Company-dependent status declared wether the startup succeeded or failed, so it was a binary classification problem (which is perfect for machine learning models), and it had no missing values, meaning we could use all of it's instances to train the model.
"""),

html.Img(src='assets/Capture.png', style={'width':'70%'}),

dcc.Markdown("""
Now we wanted to understand which features we would use to train the model. I started looking for any features that would cause data leakage, or features that were made from the information of the predicting value (wether the startup succeeded or failed after opening). We also got rid of features that did not provide any possible information on their probability of succeeding, so that the model would only be trained upon significant data. 

There was also a particular feature with all the industries the startup belonged to. However, it was formated so all the observations has their industries together as a string, something that the model would not understand well. So instead, I made a column for each respective industry, and the observation (or startup) would get a 0 if it did not belong to the industry, and a 1 if it did. 
"""),

html.Img(src='assets/download (1).png', style={'width':'50%'}),

html.Img(src='assets/download (2).png', style={'width':'70%'}),


dcc.Markdown("""
After that, I divided my dataframe into two subsets: the y, which I would be predicting, and the x, which would be the features I'd be utilizing to create the model. 
"""),


html.Img(src='assets/Capturee.png', style={'width':'60%'}),


dcc.Markdown("""
Before getting into the model, I needed a metric to act as a minimum-requirement for my model to pass. So, I estimated the accuracy of saying that all the startups belonged to the largest class, which in this cases was having the startup succeed (this dataset had a lot of startups that succeeded). The accuracy is shown below
"""),

html.Img(src='assets/download (3).png', style={'width':'70%'}),

dcc.Markdown("""
Now it was time to make the model. Two types of models were used. A logistic regressor, which returned a value from 0 to 1 (0 meaning the company failed, 1 meaning it succeeded) based on the features provided, and a XGBoost() model, which uses a form of decision trees to make it's decision. At the end, the best performing model resulted being the XGBoost model. It was given a sample of data different from what it was trained with, and these were it's results:
"""),

html.Img(src='assets/download (4).png', style={'width':'50%'}),

dcc.Markdown("""
The model was done, and it was performing quite well. Afterwards, after some parameter tuning, the model was ready for use on the web app. The model has a 95% probability of classifying startups that will succeed correctly, and a 97% chance to classify startups that will fail correctly. 
"""),


dcc.Markdown("""
*If you're interested on seeing the notebook with all the work, here's the link: https://colab.research.google.com/drive/1GGrqKB4soAxUkGui15LPPlBnMY69l4VK?usp=sharing*
""")

          
]