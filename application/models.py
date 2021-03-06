from application import db
from datetime import datetime


class Facilities(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    facility_name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(500), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    tests = db.relationship('Tests', backref='facility', lazy=True)

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    tests = db.relationship('Tests', backref='patient', lazy=True)

class Doctors(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    license_date = db.Column(db.DateTime, nullable=False)
    tests = db.relationship('Tests', backref='doctor', lazy=True)

class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    outcome = db.Column(db.String(8), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
