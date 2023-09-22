from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<div><p style=\"color:blue;\" id=\"test\"></p>\
            <img src=\"static/find_waldo.jpg\">\
            <script src=\"static/click.js\"></script>\
            </div>")