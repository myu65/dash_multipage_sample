from flask import Flask

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from pages import page1, page2

server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.CERULEAN]
)

app.title = 'テストページだよ'


navbar = dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.NavLink("page1", href="/page1")),
                    dbc.NavItem(dbc.NavLink("page2", href="/page2")),
                    dbc.NavItem(dbc.NavLink("page3", href="/page3"))
                ],
                brand="テストページだよ",
                id = 'navibar'
            )


content = html.Div(id="page-content", 
                    style={"padding": "1rem 1.5rem","width":"100%","height":"100%"})

app.layout = html.Div([
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

    if (pathname == '/page1')|(pathname == '/'): 
        return_content = page1.layout
    elif (pathname == '/page2'):
        return_content = page2.layout
       
    else:
        return_content = '404 not found'


    return [return_content]


if __name__ == "__main__":
    app.run_server(
        host = '0.0.0.0', debug=True, port='3031'
    )
    # flaskで起動する場合
    # server.run(host='0.0.0.0', port=3031, debug=True)