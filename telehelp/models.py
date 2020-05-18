from datetime import datetime
from telehelp import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    phone = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    added_on = db.Column(db.String(50), default=datetime.utcnow)
    messages = db.relationship('Message', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.name} {self.last_name}, {self.added_on}, {self.phone})'