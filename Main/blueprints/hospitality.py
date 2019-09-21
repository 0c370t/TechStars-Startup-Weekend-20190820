from flask import Blueprint, render_template

app = Blueprint("hospitality", __name__, url_prefix="/h")


@app.route("/")
def index():
    return render_template("hospitality/home.jinja.html")
