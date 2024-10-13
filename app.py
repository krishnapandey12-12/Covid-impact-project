import numpy as mp
import pandas as pd
import plotly.graph_objs as go
from dash import dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
import pandas as pd

external_stylesheet = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh',
        'crossorigin': 'anonymous'
    }
]

patients = pd.read_csv('state_wise_daily.csv')
total = patients.shape[0]
active = patients[patients['Status']=='Confirmed'].shape[0]
recovered = patients[patients['Status']=='Recovered'].shape[0]
deaths = patients[patients['Status']=='Deceased'].shape[0]

options=[
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'},
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)


app.layout = html.Div([
    html.H1('Corona Virus Pandamic',
            style={'color': ' #fff',
                   'text-align': 'centre'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', className='text-light'),
                    html.H4(total, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active cases', className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered cases', className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Death', className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3')
    ], className='row'),
    html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    dcc.Dropdown(id= 'picker',options =options, value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')

    ], className='row')
],className='container')

@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(type):

    if type == 'All':
        return{'data': [go.Bar(x=patients['State'],y=patients['Total'])],
               'layout': go.Layout(title='State Total Count',plot_bgcolor='orange')}
    if type == 'Hospitalized':
        return{'data': [go.Bar(x=patients['State'],y=patients['Hospitalized'])],
               'layout': go.Layout(title='State Total Count',plot_bgcolor='orange')}
    if type == 'Recovered':
        return{'data': [go.Bar(x=patients['State'],y=patients['Recovered'])],
               'layout': go.Layout(title='State Total Count',plot_bgcolor='orange')}
    if type == 'Deceased':
        return{'data': [go.Bar(x=patients['State'],y=patients['Deceased'])],
               'layout': go.Layout(title='State Total Count',plot_bgcolor='orange')}


if __name__ == '__main__':
    app.run_server(debug=True)