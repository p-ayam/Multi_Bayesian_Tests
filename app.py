# Running on Windows, platform.version()  '10.0.19042'


# !python --version
# Python 3.9.5


#import pandas as pd # pd.__version__  '1.2.4'
#import numpy as np # np.__version__ '1.20.3'
#from numpy import arange


# Importing the required libraries
import numpy as np

import plotly.graph_objects as go # plotly 4.14.1
from plotly.subplots import make_subplots
import dash  # print(dash.__version__) (version 1.18.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc # version 0.11.1





####### Data Dashboard

# Importing the required libraries
import plotly.graph_objects as go # plotly 4.14.1
from plotly.subplots import make_subplots
import dash  # print(dash.__version__) (version 1.18.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc # version 0.11.1
import dash_html_components as html
import dash_daq as daq


# --------------Dash App Layout----------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])



#application = app.server
server = app.server
app.title='Multiple Bayes Tests'




app.layout = dbc.Container([


    dbc.Row(
        dbc.Col(dcc.Markdown(''' ''',
                             className=' font-weight-bold text-left text-muted text-primary mb-sm-5'),
                width={'size': 10, 'offset': 1, 'order': 1}), justify='start'),


    dbc.Row(
        dbc.Col(html.H5('Bayesian Tests',
                        className=' font-weight-bold text-center text-muted text-primary mb-sm-5'),
                width=10), justify='center'),
    
  
################## INPUT ########

    dbc.Row([

        dbc.Col([
            html.H6('No. Positive Results' )
        ],className='text-right text-primary', #width={'size': 5, 'offset': 1, 'order': 1}, #xs=6, sm=12, md=12, lg=5, xl=5
        ),
        
        
        dbc.Col([
            html.H6('No. Negative Results' )
        ],className='text-left text-primary', #width={'size': 5, 'offset': 0, 'order': 1}, #xs=6, sm=12, md=12, lg=5, xl=5
        )
        
  ], justify='left'),

###################      
    dbc.Row(
          html.Div([      
              dcc.Input(id="input_pos", type="number", value=0, placeholder="", min=0, style={'marginRight':'1px'}),
              dcc.Input(id="input_negat", type="number", value=1,  placeholder="", min=0, style={'marginRight':'1px'}),
          ])
   
       ,justify='center' ),#justify='center'),
    
    
    
    dbc.Row(
        dbc.Col(dcc.Markdown('''  ''',
                             className=' font-weight-bold text-left text-muted text-primary mb-sm-5'),
                width={'size': 2, 'offset': 1, 'order': 1}), justify='start'),
    

    #####################
    dbc.Row([

        dbc.Col([
            html.H6('7-Day Incidence / 100K' )
        ],className='text-center text-primary', width={'size': 3, 'offset': 0, 'order': 1}, #xs=12, sm=12, md=12, lg=5, xl=5
        ),
        
        
        dbc.Col([
            html.H6('Sensitivity %' )
        ],className='text-left text-primary', width={'size': 2, 'offset': 0, 'order': 1}, #xs=12, sm=12, md=12, lg=5, xl=5
        ),
        
        dbc.Col([
            html.H6('Specificity %' )
        ],className='text-left text-primary', width={'size': 2, 'offset': 0, 'order': 1}, #xs=12, sm=12, md=12, lg=5, xl=5
        )
        
  ], justify='center'),
        
    ###################
    
    dbc.Row(


          html.Div([
              dcc.Input(id="input_index", type="number",value=100,   placeholder="50", min=0,max=10**5),
              dcc.Input(id="input_sen", type="number",  value=80,  placeholder="80", min=0, max=100),
              dcc.Input(id="input_spec", type="number",value=98,  placeholder="98", min=0,max=100)
          ])
   
       ,justify='center' ),
##################
   
    dbc.Row(
        dbc.Col(dcc.Markdown(''' ''',
                             className=' font-weight-bold text-left text-muted text-primary mb-sm-5'),
                width={'size': 10, 'offset': 1, 'order': 1}), justify='start'),




################## OutPUT ########

   
   
    dbc.Row([ dbc.Col([

                daq.Gauge(
                    id='gauge_id',
                    size=350,
                    #color={"gradient":True,"ranges":{"green":[-5,-3],"yellow":[-3,-1],"red":[-1,0]}},
                    color={'default':'#9B51E0', 'gradient':True},#"#9B51E0",

                    
                    scale={'start': -5, 'interval': 1 ,'labelInterval': 1},
                    logarithmic=True,
                    #base=10,
                    #value=40,
                    #label='Probability of Being Infected',
                    max=0,
                    min=-5
                )
        
    ])
            ], justify='center') ,




    ], fluid=False)


# -------------------App Callback-------------------

@app.callback(
    #Output('Polymer_NIR', 'figure'),
    #Output(component_id='div_output', component_property='value'),
    Output('gauge_id', 'value'),
    Output('gauge_id', 'label'),
    
    Input('input_pos', 'value'),
    Input('input_negat', 'value'),
    Input('input_index', 'value'),
    Input('input_sen', 'value'),
    Input('input_spec', 'value'))



def update_output(posit_no, negat_no, input_index, sens_perc , spec_perc):
    
    
    prior= float(input_index) / 10**5 # converting 7-day incidence to prior probability
    sens= float(sens_perc) / 100
    spec = float(spec_perc) / 100
    p = ((sens**posit_no) * ( (1-sens)**negat_no ) * prior) / ( (sens**posit_no) * ((1-sens)**negat_no) * prior + \
                                                         ((1-spec)**posit_no) * (spec**negat_no) * (1-prior) )
    txt= 'Probability of Actualy Being Positive = ' + str(round(p*100,3)) + ' %'
    
#     print('posit_no',posit_no)
#     print('negat_no',negat_no)
#     print( 'input_index',input_index)
#     print(     'sens_perc', sens_perc) 
#     print(      'spec_perc',spec_perc)
#     print('prior',prior)
#     print('sens',sens)
#     print('spec',spec)
#     print(np.log10(p))
    
#     print(p)


    return(p , txt)


#-------run the app ------------
if __name__=='__main__':
#    application.run(port=8080)
#    app.run_server(port=8080)
    app.run_server(debug=False, host="0.0.0.0", port=8000)
#    application.run(debug=True, port=8080)
#    app.run_server(debug=True,port=8050)
#    app.server.run(debug=True, host='0.0.0.0')
#    app.run_server(debug=True, port=8050, host='0.0.0.0')
#    app.run_server(debug=True, port=7000, host='0.0.0.0')
#    application.run(debug=True, port=8080)
#    app.run_server(debug=True, port=7000)
#    for Jupyter notebook
#    app.server.run(port=3000, host='127.0.0.1')
#    app.server.run(debug=True, port=3000, host='0.0.0.0')





