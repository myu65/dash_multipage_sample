from dash import dcc, html, Input, Output, callback

PAGE_ID = 'page2'

layout = html.Div([
    html.H3('Page 2'),
    dcc.Dropdown(
        {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
        id=f'{PAGE_ID}_dropdown'
    ),
    html.Div(id=f'{PAGE_ID}_display-value'),
    dcc.Link('Go to Page 1', href='/page1')
])


@callback(
    Output(f'{PAGE_ID}_display-value', 'children'),
    Input(f'{PAGE_ID}_dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'