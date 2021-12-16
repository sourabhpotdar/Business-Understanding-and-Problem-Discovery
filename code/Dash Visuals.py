## Dash Visualisation for YFinance Module

#Importing Libraries
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)




# Initialising App Name
app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("Output.csv")
print(df[:5])

# ------------------------------------------------------------------------------
# App layout
# Adding all the html contents that needs to be added in the appliction
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    # Creating filter for the graphs
    dcc.Dropdown(id="slct_ticker",
                 options=[
                     {"label": "GOOG", "value": "GOOG"},
                     {"label": "TSLA", "value": "TSLA"},
                     {"label": "NFLX", "value": "NFLX"}],
                 multi=False,
                 value="GOOG",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    # Drawing line charts 
    dcc.Graph(id='my_line_chart', figure={}),
    
    # Drawing candle stick chart.
    dcc.Graph(id='my_candle_stick', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'), #output graphs that needs to be shown on the html page
     Output(component_id='my_line_chart', component_property='figure'),
     Output(component_id='my_candle_stick', component_property='figure')],
    [Input(component_id='slct_ticker', component_property='value')] # Filter input variable
)
# Creating funtion to link all the components and applying filter conditions and doing alll the calculation for the graphs.
def update_graph(option_slctd):
    print(option_slctd) # Displaying the selected filter
    print(type(option_slctd))

    container = "The ticker value chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["TickerName"] == option_slctd] # Applying the filter condition on the dataset

    # Plotly Express Creating line graph
    fig1 = go.Figure([go.Scatter(x=dff['Date'], y=dff['Volume'])])

    # Plotly Express Creating Candlestick chart
    fig2 = go.Figure(data=[go.Candlestick(x=dff['Date'],
                open=dff['Open'],
                high=dff['High'],
                low=dff['Low'],
                close=dff['Close'])])

    return container, fig1, fig2 # returning all the output variables


# ------------------------------------------------------------------------------
# Calling App to run the local server.
if __name__ == '__main__':
    app.run_server(debug=True)