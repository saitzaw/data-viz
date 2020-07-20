import dash_html_components as html 

layout = html.Div([
    html.Button('Click me', id='btn'),
    html.Div(id='output')
])