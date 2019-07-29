# from database.db_setup import *
# from model.building import *
from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime, timedelta
db = SQLAlchemy(app)

def exp_date():
    return datetime.utcnow() + timedelta(days=30)

class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    visitcount = db.Column(db.Integer)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    expiration_date = db.Column(db.DateTime, default=exp_date)


def init_db():
    db.create_all()
    print("Database created")
