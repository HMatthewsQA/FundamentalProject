from application import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id)

class Facilities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Facility_name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(500), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    DOB = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

class Doctors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    DOB = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    license_date = db.Column(db.DateTime, nullable=False)

class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    outcome = db.Column(db.String(8), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
