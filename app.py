import dash
from app.layouts.layout import layout
from app.callbacks import register_callbacks
import pandas as pd 

external_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheet)
df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
available_indicators = df['Indicator Name'].unique()
app.layout = layout(available_indicators,df)
register_callbacks(app,df)

if __name__=='__main__': 
    """ 
    run the flask server 
    """ 
    app.run_server(debug=True)