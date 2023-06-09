from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json

admin = Blueprint('admin', __name__)

@admin.route('/', methods=['GET', 'POST'])
@login_required
def administrator():
    if current_user.email != "tejus3131@gmail.com":
        return redirect(url_for('views.home'))
    else:
        return render_template("admin.html", user = current_user)
