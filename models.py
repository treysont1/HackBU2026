from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

class StudySession(db.Model):
    id = db.column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(200))

    participants = db.Column(db.Integer, default=1)
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

