from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET'])
def userAuthentication():
    return render_template("userAuthentication.html", user = None)

@auth.route('/checkAuth')
def checkAuth():
    if current_user.is_authenticated:
        return redirect(url_for('auth.logout'))
    else:
        return redirect(url_for('auth.userAuthentication'))

@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('loginEmail')
    password = request.form.get('loginPassword')
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Email does not exist.', category='error')
    return redirect(url_for('auth.userAuthentication'))




@auth.route('/register', methods=['POST'])
def sign_up():
    email = request.form.get('registerEmail')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    password1 = request.form.get('registerPassword')
    password2 = request.form.get('registerRepeatPassword')
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists.', category='error')
    elif len(email) < 4:
        flash('Email must be greater than 3 characters.', category='error')
    elif len(first_name) < 2:
        flash('First name must be greater than 1 character.', category='error')
    elif len(last_name) < 2:
        flash('Last name must be greater than 1 character.', category='error')
    elif password1 != password2:
        flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
        flash('Password must be at least 7 characters.', category='error')
    else:
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(
            password1, method='scrypt'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
        return redirect(url_for('views.home'))
    return redirect(url_for('auth.userAuthentication'))

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('logged out!', category='success')
    return redirect(url_for('views.index'))