import dash
from app.layout import layout
from app.callbacks import register_callbacks

app = dash.Dash()
app.layout = layout
register_callbacks(app)

if __name__=='__main__': 
    app.run_server(debug=True)