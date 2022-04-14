from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H3('Page 2'),
    dcc.Dropdown(
        {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
        id='dropdown'
    ),
    html.Div(id='display-value'),
    dcc.Link('Go to Page 1', href='/page1')
])


@callback(
    Output('display-value', 'children'),
    Input('dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'