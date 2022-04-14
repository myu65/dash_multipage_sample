from flask import Flask


app = Flask(__name__)

with app.app_context():
    from pages.navbar import add_dash as ad_navbar
    app = ad_navbar(app)


    from pages.page1 import add_dash as ad_page1
    app = ad_page1(app)

    from pages.page2 import add_dash as ad_page2
    app = ad_page2(app)

if __name__ == "__main__":
    # flaskで起動する場合
    app.run(host='0.0.0.0', port=3031, debug=True)