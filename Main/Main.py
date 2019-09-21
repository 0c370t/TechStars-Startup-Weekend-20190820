from flask import Flask, render_template
from Main.api import cleaners, tenants

app = Flask(__name__)


@app.route("/")
def index():
    recent_cleaners = cleaners.getMostRecentCleaners()
    upcoming_tenants = tenants.getTenants()
    return render_template("homeowner.jinja.html", tenants=upcoming_tenants, cleaners=recent_cleaners)
