from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Facilities, Patients, Doctors, Tests
from application.forms import UpdatePatientForm, RegisterFacilityForm, RegisterPatientForm, RegisterDoctorForm, TestForm, DeleteForm

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

@app.route('/patients/update', methods=['GET', 'POST'])
def update_patient():
    form = UpdatePatientForm()
    if form.validate_on_submit():
        patient = Patients.query.filter_by(id=form.id.data).first()
        patient.first_name = form.first_name.data
        patient.last_name = form.last_name.data
        patient.dob = form.dob.data
        patient.gender = form.gender.data
        patient.address = form.address.data
        patient.telephone = form.telephone.data
        patient.email = form.email.data
        db.session.commit()
        return redirect(url_for('patients'))
    return render_template('update_patient.html', title='UpdatePatient',form=form)

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

@app.route('/tests/register', methods=['GET', 'POST'])
def register_test():
    form = TestForm()
    if form.validate_on_submit():
        doctor = Doctors.query.filter_by(id=form.doctor.data).first()
        facility = Facilities.query.filter_by(id=form.facility.data).first()
        patient = Patients.query.filter_by(id=form.patient.data).first()
        test = Tests(
                outcome = form.outcome.data,
                facility = facility,
                patient = patient,
                doctor = doctor
        )
        db.session.add(test)
        db.session.commit()
        return redirect(url_for('tests'))
    return render_template('register_test.html', title='RegisterTest:',form=form)

@app.route('/tests/delete', methods=['GET', 'POST'])
def delete_test():
    form = DeleteForm()
    if form.validate_on_submit():
        test = Tests.query.filter_by(id=form.id.data).first()
        db.session.delete(test)
        db.session.commit()
        return redirect(url_for('tests'))
    return render_template('delete_test.html', title='DeleteTest', form=form)
