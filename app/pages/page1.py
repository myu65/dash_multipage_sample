from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H3('Page 1'),
    dcc.Dropdown(
        {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
        id='dropdown'
    ),
    html.Div(id='display-value'),
    dcc.Link('Go to Page 2', href='/page2')
])


@callback(
    Output('display-value', 'children'),
    Input('dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'