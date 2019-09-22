from flask import Blueprint, render_template

app = Blueprint("tenant", __name__, url_prefix="/t")


@app.route("/")
def index():
    return render_template("tenant/home.jinja.html")

