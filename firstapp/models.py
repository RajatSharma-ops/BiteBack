from app import db
from flask_login import UserMixin

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    food_item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    is_booked = db.Column(db.Boolean, nullable=False , default=False)


#user model
class User(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True ,autoincrement=True )
     U_name = db.Column(db.String(100), nullable=False)
     U_email = db.Column(db.String(150), unique=True, nullable=False)
     password = db.Column(db.String(200), nullable=False)
