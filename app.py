import dash
import pandas as pd
from dash import html, dcc, Input, Output
import altair as alt

# Read data
wine = pd.read_csv("data/winequality-red.csv")

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='iframe',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='ycol-widget',
        value='pH',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in wine.columns])])

# Set up callbacks/backend
@app.callback(
    Output('iframe', 'srcDoc'),
    Input('ycol-widget', 'value'))
def plot_altair(ycol):
    chart = alt.Chart(wine).mark_point().encode(
        y=ycol,
        x='pH',
        tooltip='pH').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)