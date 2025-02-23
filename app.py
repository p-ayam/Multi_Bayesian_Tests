import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
app.title = 'Multiple Bayes Tests'

app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(dcc.Markdown(''' ''',
                             className=' font-weight-bold text-left text-muted text-primary mb-sm-5'),
                width={'size': 10, 'offset': 1, 'order': 1}), justify='start'),

    dbc.Row(
        dbc.Col(html.H5('Bayesian Tests',
                        className=' font-weight-bold text-center text-muted text-primary mb-sm-5'),
                width=10), justify='center'),

    dbc.Row([

        dbc.Col([
            html.H6('No. Positive Results..............No. Negative Results')
        ], className='text-left',
            width={'size': 15, 'offset': 0, 'order': 1}, #xs=6, sm=12, md=12, lg=5, xl=5
        ),
    ], justify='center'),

    dbc.Row(
        html.Div([
            dcc.Input(id="input_pos", type="number", value=0, placeholder="", min=0, style={'marginRight': '1px'}),
            dcc.Input(id="input_negat", type="number", value=1, placeholder="", min=0, style={'marginRight': '1px'}),
        ])

        , justify='center'),  # justify='center'),

    dbc.Row(
        dbc.Col(dcc.Markdown('''  ''',
                             className=' font-weight-bold text-left text-muted text-primary mb-sm-5'),
                width={'size': 2, 'offset': 1, 'order': 1}), justify='start'),

    dbc.Row([

        dbc.Col([
            html.H6('7-Day Incidence / 100K..................Sensitivity %.........................Specificity %')
        ], className='text-left', width={'size': 15, 'offset': 0, 'order': 1},
        ),
    ], justify='center'),


    dbc.Row(

        html.Div([
            dcc.Input(id="input_index", type="number", value=100, placeholder="50", min=0, max=10 ** 5),
            dcc.Input(id="input_sen", type="number", value=80, placeholder="80", min=0, max=100),
            dcc.Input(id="input_spec", type="number", value=98, placeholder="98", min=0, max=100)
        ])

        , justify='center'),
    ##################

    dbc.Row(
        dbc.Col(dcc.Markdown(''' ''',
                             className=' font-weight-bold text-left text-muted text-primary mb-sm-5'),
                width={'size': 10, 'offset': 1, 'order': 1}), justify='start'),

    dbc.Row([dbc.Col([

        daq.Gauge(
            id='gauge_id',
            size=350,
            color={'default': '#9B51E0', 'gradient': True},  # "#9B51E0",
            scale={'start': -5, 'interval': 1, 'labelInterval': 1},
            logarithmic=True,
            max=0,
            min=-5
        )
    ])
    ], justify='center'),

], fluid=False)


# -------------------App Callback-------------------

@app.callback(
    Output('gauge_id', 'value'),
    Output('gauge_id', 'label'),

    Input('input_pos', 'value'),
    Input('input_negat', 'value'),
    Input('input_index', 'value'),
    Input('input_sen', 'value'),
    Input('input_spec', 'value'))
def update_output(posit_no, negat_no, input_index, sens_perc, spec_perc):
    prior = float(input_index) / 10 ** 5  # converting 7-day incidence to prior probability
    sens = float(sens_perc) / 100
    spec = float(spec_perc) / 100
    p = ((sens ** posit_no) * ((1 - sens) ** negat_no) * prior) / (
                (sens ** posit_no) * ((1 - sens) ** negat_no) * prior + \
                ((1 - spec) ** posit_no) * (spec ** negat_no) * (1 - prior))
    txt = 'Probability of Actualy Being Positive = ' + str(round(p * 100, 3)) + ' %'


    return (p, txt)

if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8000)






