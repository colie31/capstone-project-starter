from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Category(db.Model, UserMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)