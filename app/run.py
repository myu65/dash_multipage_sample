from flask import Flask

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
)

app.title = 'テストページだよ'


navbar = dbc.NavbarSimple(
                children=[],
                brand="テストページだよ",
                color="dark",
                dark=True,
                fluid=True,
                id = 'navibar'
            )


content = html.Div(id="page-content", 
                    style={"padding": "1rem 1.5rem","width":"100%","height":"100%"})

app.layout = html.Div([
                        dcc.Store(id='side_click'),
                        dcc.Location(id='url', refresh=False),
                        navbar,
                        content
                    ])


@app.callback(
    [
        Output('page-content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def display_page(pathname):

    tab = [
        dbc.NavItem(dbc.NavLink("page1", href="/page1")),
        dbc.NavItem(dbc.NavLink("page2", href="/page2"))
    ]

    if (pathname == '/page1'): 
        return_content = html.Div('ページ１だよ')
    elif (pathname == '/page2':
        return_content = html.Div('ページ２だよ')
       
    else:
        return_content = '404 Page not found'


    return [return_content]


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=3031, debug=True)