from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        user = current_user
    else:
        user = None
    return render_template("index.html", user=user)

@views.route('/home', methods=['GET'])
@login_required
def home():
    return render_template("home.html", user = current_user)

@views.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template("profile.html", user = current_user)

@views.route('/about', methods=['GET'])
def about():
    return render_template("about.html", user = current_user)

@views.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", user = current_user)