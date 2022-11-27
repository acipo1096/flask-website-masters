from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact (db.Model):
    __tablename__ = 'website_contact'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(80), unique=False, nullable=False)

def __init__(self, user_id, name, email, message):
    self.user_id = user_id
    self.name = name
    self.email = email
    self.message = message