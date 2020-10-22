from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from joblib import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly.tools import mpl_to_plotly
import seaborn as sns
import xlrd

from app import app

pipeline = load('model/new_pipeline.joblib')
X = pd.read_csv('model/X-features.csv', index_col=0)
y = pd.read_csv('model/y-features.csv', index_col=0)

X.drop('year of founding', axis=1, inplace=True)
y.replace('Success', 1, inplace=True)
y.replace('Failed', 0, inplace=True)
y = y.astype(float)



y_pred = pipeline.predict(X)
y_pred = np.where(y_pred=='Success', 1, y_pred)
y_pred = np.where(y_pred=='Failed', 0, y_pred)
y_pred = y_pred.astype(float)



fig, ax = plt.subplots()
sns.distplot(y['Dependent-Company Status'], hist=False, kde=True, ax=ax, label='Actual')
sns.distplot(y_pred, hist=False, kde=True, ax=ax, label='Predicted')
# ax.set_title('Distribution of Actual Exit compared to prediction')
ax.legend().set_visible(False)
#ax.set(ylabel='Total Guests (muliply by 100)', xlabel='0 = Non-Perm, 1 = Perm Exit')

# plt.xlabel('0 = Non-Perm Exit, 1 = Perm Exit', fontsize=18)
# plt.ylabel('Total Guests (multiply # by 100)', fontsize=18)

plotly_fig = mpl_to_plotly(fig)
plotly_fig['layout']['showlegend'] = True


layout = [dcc.Markdown("""
### Evaluate
This graph shows the actual distribution of startups based on their success or failure vs. the predicted distribution. As you can see, they are not that far apart, which helps visualize the accuracy of our plot.
"""), 

dcc.Graph(id='evaluate-graph', figure=plotly_fig)
]