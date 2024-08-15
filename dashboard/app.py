import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load a sample dataset
df = px.data.gapminder()

# Filter the dataset for a specific year
df = df[df['year'] == 2007]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Simple Dash Dashboard'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='United States',
        clearable=False
    ),

    dcc.Graph(
        id='life-exp-vs-gdp',
    )
])


@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    Input('country-dropdown', 'value')
)
def update_figure(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',
                     size='pop', color='continent', hover_name='country',
                     log_x=True, size_max=60)
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
