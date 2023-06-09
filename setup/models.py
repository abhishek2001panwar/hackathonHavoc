from . import db
from flask_login import UserMixin


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(10000))
    progress = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    courses = db.relationship('Course')
