from flask import Flask, render_template
from Main.blueprints import hospitality, tenant, homeowner

app = Flask(__name__)

app.register_blueprint(hospitality)
app.register_blueprint(homeowner)
app.register_blueprint(tenant)

@app.route("/")
def index():
    return render_template("index.jinja.html")
