import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Plotly Dash Web App'),
    html.Div(children='''
        A simple web app using Dash and Plotly.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=px.line(x=[1, 2, 3, 4, 5], y=[1, 3, 2, 5, 4])
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

