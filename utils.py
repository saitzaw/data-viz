import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]) ])

def get_header(app):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        html.Br()
                    ), 
                    html.Div(
                        [html.H5("")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )

def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ])
