from .db import db
from flask_login import UserMixin

class Journal(db.Model, UserMixin):
    __tablename__ = 'journals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id')) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    color = db.relationship('Color', back_populates='journals')
    user = db.relationship('User', back_populates='journals')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color.shade,
            'user': self.user.username
            }