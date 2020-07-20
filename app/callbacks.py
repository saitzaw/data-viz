from dash.dependencies import Output, Input
import pandas as pd 
import plotly.express as px

def register_callbacks(app,df): 
    @app.callback(
        Output('indicator-graphic', 'figure'),
        [Input('xaxis-column', 'value'),
        Input('yaxis-column', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        Input('year--slider', 'value')])

    def update_graph(xaxis_column_name, yaxis_column_name,xaxis_type, yaxis_type,year_value):
        dff = df[df['Year'] == year_value]

        fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                        y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                        hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

        fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

        fig.update_xaxes(title=xaxis_column_name, 
                        type='linear' if xaxis_type == 'Linear' else 'log') 

        fig.update_yaxes(title=yaxis_column_name, 
                        type='linear' if yaxis_type == 'Linear' else 'log') 

        return fig

