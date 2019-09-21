from flask import Flask, render_template
from Main.api import cleaners, tenants
from Main.blueprints import hospitality
from Main.blueprints import homeowner
app = Flask(__name__)
app.register_blueprint(hospitality)
app.register_blueprint(homeowner)

@app.route("/")
def index():
    recent_cleaners = cleaners.getMostRecentCleaners()
    upcoming_tenants = tenants.getTenants()
    return render_template("homeowner/home.jinja.html", tenants=upcoming_tenants, cleaners=recent_cleaners)


@app.route("/2")
def index2():
    return render_template("hospitality/home.jinja.html")
