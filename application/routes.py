from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Facilities, Patients, Doctors, Tests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home:')

@app.route('/facilities')
def facilities():
    all_facilities = Facilities.query.all()
    return render_template('facilities.html', title='Facilities:', facilities=all_facilities)

@app.route('/patients')
def patients():
    all_patients = Patients.query.all()
    return render_template('patients.html', title='Patients:', patients=all_patients)

@app.route('/doctors')
def doctors():
    all_doctors = Doctors.query.all()
    return render_template('doctors.html', title='Doctors:', doctors=all_doctors)

@app.route('/tests')
def tests():
    all_tests = Tests.query.all()
    return render_template('tests.html', title='Tests:', tests=all_tests)
