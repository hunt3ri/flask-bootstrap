from flask import render_template

from app import APP_NAME
from app.web import main


@main.route("/")
def home_page():
    """
    Controller to launch simple home page.  While flask can host SPA's better to host SPA separately.  Alternatively
    you can always create apps with flask templates and Jinja :)
    """
    return render_template("home.html", app_name=APP_NAME)
