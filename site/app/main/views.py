from flask import render_template, request, redirect, url_for, abort, current_app, flash
from . import main
from .. import db
from flask import jsonify

@main.route("/")
def index():
    return render_template("main-page.html")
