from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc



def add_dash(server):
    UBPATH = '/pages/page2/'
    app = Dash(
        __name__,
        server=server,
        url_base_pathname=UBPATH,
        suppress_callback_exceptions=True,
        external_stylesheets=[dbc.themes.CERULEAN]
    )


    app.layout = html.Div([
        html.H3('Page 2'),
        dcc.Dropdown(
            {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
            id='dropdown'
        ),
        html.Div(id='display-value'),
        dcc.Link('Go to Page 1', href='../../page1', target='parent')
    ])


    @app.callback(
        Output('display-value', 'children'),
        Input('dropdown', 'value'))
    def display_value(value):
        return f'You have selected {value}'

    return server