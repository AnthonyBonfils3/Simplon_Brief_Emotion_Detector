import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
from app import app
from my_imports.my_var import modal

layoutHome = html.Div(id='app-homePage', children=[

    dcc.Link(html.Button('Datas analysis', className='pth_button'), href='/Datas%20Analysis'),
    dcc.Link(html.Button('Classifications results', className='pth_button'), href="/Classifications%20Results"),
    html.Br(),
    html.H1('Emotions Detector'),
    html.Br(),
    html.Div(id='Block_home_Page', children=[
        html.Section(id='home_page_left', children=[
            html.Br(),
            html.H2('Welcome to the API who analyse emotions in your sentences'),
            html.Br(),
            modal,
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            dcc.Textarea(
                id='text_box_home',
                placeholder='Enter your text and show the predicted emotion',
                #style={'width': '95%', 'color':'#91dfd2'}
            ),
            html.Br(),
            html.Div(id='div_submit_button', children=[
                html.Button('Submit', id='submit_button', n_clicks=0),
            ]),
            html.Div(id='output_container'),      
               
        ]),

        html.Section(id='home_page_right', children=[
            html.Div(id='div_roue', children=[
                html.Img(id='img_roue', src=app.get_asset_url('/Images/roue_des_emotions.png')),
            ]),
        ]),    
    ]),

    ## Footer
    html.Br(),
    dcc.Link(html.Button('Datas analysis', className='pth_button'), href='/Datas%20Analysis'),
    dcc.Link(html.Button('Classifications results', className='pth_button'), href="/Classifications%20Results"),
])

