from flask import Blueprint, render_template
from Main.api import cleaners, tenants
 
app = Blueprint("homeowner", __name__, url_prefix="/o")


@app.route("/")
def index():
    recent_cleaners = cleaners.getMostRecentCleaners()
    upcoming_tenants = tenants.getTenants()
    return render_template("homeowner/home.jinja.html", tenants=upcoming_tenants, cleaners=recent_cleaners)

