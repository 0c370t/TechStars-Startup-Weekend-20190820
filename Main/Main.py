from flask import Flask, render_template
from Main.api import cleaners, tenants
from Main.blueprints import hospitality
from Main.blueprints import homeowner
app = Flask(__name__)
app.register_blueprint(hospitality)
app.register_blueprint(homeowner)

@app.route("/")
def index():
    return render_template("index.jinja.html")
