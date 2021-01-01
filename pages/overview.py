import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_president_tenure = pd.read_csv(DATA_PATH.joinpath("df_mmr_president_tenure.csv"))
df_president_data = pd.read_csv(DATA_PATH.joinpath("df_president_data.csv"))



def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("မြန်မာ့နိုင်ငံတော် သမ္မတများ"),
                                    html.Br([]),
                                    html.P(
                                        "မြန်မာနိုင်ငံ လွတ်လပ်ရေးရပြီးသည်မှ စ၍ နိုင်ငံတော်၏အကြီးအမှူးအဖြစ် \
                                        ပါလီမန်ဒီမိုကရေစီ၊ ဆိုရှယ်လစ်စနစ်နှင့် ပါတီစုံဒီမိုကရေစီ အထိ \
                                        ခေတ်အဆက်ဆက် တာဝန်ထမ်းဆောင်ခဲ့ကြသည့်သမ္မတများ",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["သမ္မတတာဝန်ထမ်းဆောင်ချိန်"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_president_tenure)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["သမ္မတ၏နောက်ခံပါတီ"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_president_data)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
