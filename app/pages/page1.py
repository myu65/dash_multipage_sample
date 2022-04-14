from dash import dcc, html, Input, Output, callback

PAGE_ID = 'page1'

layout = html.Div([
    html.H3('Page 1'),
    dcc.Dropdown(
        {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
        id= f'{PAGE_ID}_dropdown'
    ),
    html.Div(id=f'{PAGE_ID}_display-value'),
    dcc.Link('Go to Page 2', href='/page2')
])


@callback(
    Output(f'{PAGE_ID}_display-value', 'children'),
    Input(f'{PAGE_ID}_dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'