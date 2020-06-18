from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Facilities, Patients, Doctors, Tests
from application.forms import RegisterFacilityForm, RegisterPatientForm, RegisterDoctorForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home:')

@app.route('/facilities', methods=['GET'])
def facilities():
    all_facilities = Facilities.query.all()
    return render_template('facilities.html', title='Facilities:', facilities=all_facilities )

@app.route('/facilities/register', methods=['GET', 'POST'])
def register_facility():
    form = RegisterFacilityForm()
    if form.validate_on_submit():
        facility = Facilities(
                facility_name = form.facility_name.data,
                address = form.address.data,
                capacity = form.capacity.data
        )
        db.session.add(facility)
        db.session.commit()
        return redirect(url_for('facilities'))
    return render_template('register_facility.html', title='RegisterFacility',form=form)

@app.route('/patients', methods=['GET'])
def patients():
    all_patients = Patients.query.all()
    return render_template('patients.html', title='Patients:', patients=all_patients)

@app.route('/patients/register', methods=['GET', 'POST'])
def register_patient():    
    form = RegisterPatientForm()
    if form.validate_on_submit():
        patient = Patients(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                dob = form.dob.data,
                gender = form.gender.data,
                address = form.address.data,
                telephone = form.telephone.data,
                email = form.email.data
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patients'))
    return render_template('register_patient.html', title='RegisterPatient',form=form)

@app.route('/doctors')
def doctors():  
    all_doctors = Doctors.query.all()
    return render_template('doctors.html', title='Doctors:', doctors=all_doctors)

@app.route('/doctors/register', methods=['GET', 'POST'])
def register_doctor():
    form = RegisterDoctorForm()
    if form.validate_on_submit():
        doctor = Doctors(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                dob = form.dob.data,
                gender = form.gender.data,
                license_date = form.license_date.data
        )
        db.session.add(doctor)
        db.session.commit()
        return redirect(url_for('doctors'))
    return render_template('register_doctor.html', title='RegigsterDoctor', form=form)

@app.route('/tests')
def tests():
    all_tests = Tests.query.all()
    return render_template('tests.html', title='Tests:', tests=all_tests)

@app.route('/tests/register')
def register_test():
    return render_template('register_test.html', title='RegisterTest:')
