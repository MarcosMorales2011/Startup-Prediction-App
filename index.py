from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from tabs import intro, predict, process, insights

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Lending Club interest rates'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Intro', value='tab-intro'), 
        dcc.Tab(label='Predict', value='tab-predict'), 
        dcc.Tab(label='Process', value='tab-process'), 
        dcc.Tab(label='Insights', value='tab-insights')
    ]),
    html.Div(id='tabs-content')
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-process': return process.layout
    elif tab == 'tab-insights': return insights.layout

if __name__ == '__main__':
    app.run_server(debug=True)