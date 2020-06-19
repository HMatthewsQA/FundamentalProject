from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Facilities, Patients, Doctors, Tests

class RegisterFacilityForm(FlaskForm):
    facility_name = StringField('Facility Name',
            validators = [
                DataRequired(),
                Length(min=2, max=100)
                ])
    address = StringField('Address',
            validators = [
                DataRequired(),
                Length(min=2, max=500)
                ])
    capacity = IntegerField('Capacity',
            validators = [
                DataRequired()
                ])
    submit = SubmitField('Add Facility')

class RegisterPatientForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    dob = DateField('Data of Birth: d/m/y', format='%d/%m/%y',
            validators = [
                DataRequired()
                ])
    gender = StringField('Gender: M/F',
            validators = [
                DataRequired(),
                Length(min=1, max = 1)
                ])
    address = StringField('Address',
            validators = [
                DataRequired(),
                Length(min=2, max=500)
                ])
    telephone = StringField('Telephone no.',
            validators = [
                DataRequired(),
                Length(min=11, max=11)
                ])
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
                ])
    submit = SubmitField('Add Patient')

class RegisterDoctorForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    dob = DateField('Data of Birth: d/m/y', format='%d/%m/%y',
            validators = [
                DataRequired()
                ])
    gender = StringField('Gender: M/F',
            validators = [
                DataRequired(),
                Length(min=1, max = 1)
                ])
    license_date = DateField('License Date: d/m/y', format='%d/%m/%y',
            validators = [
                DataRequired()
                ])
    submit = SubmitField('Add Doctor')

class TestForm(FlaskForm):
    outcome = StringField('Outcome: Postive/Negative',
            validators = [
                DataRequired(),
                Length(min=8, max=8)
                ])
    patient = IntegerField('PatientID:',
            validators = [
                DataRequired()
                ])
    facility = IntegerField('FacilityID:',
            validators = [
                DataRequired()
                ])
    doctor = IntegerField('DoctorID:',
            validators = [
                DataRequired()
                ])
    submit = SubmitField('Add Test')

class UpdatePatientForm(FlaskForm):
    id = IntegerField('PatientID',
            validators = [
                DataRequired()
                ])
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
                ])
    dob = DateField('Data of Birth: d/m/y', format='%d/%m/%y',
            validators = [
                DataRequired()
                ])
    gender = StringField('Gender: M/F',
            validators = [
                DataRequired(),
                Length(min=1, max = 1)
                ])
    address = StringField('Address',
            validators = [
                DataRequired(),
                Length(min=2, max=500)
                ])
    telephone = StringField('Telephone no.',
            validators = [
                DataRequired(),
                Length(min=11, max=11)
                ])
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
                ])
    submit = SubmitField('Update')

class DeleteForm(FlaskForm):
    id = IntegerField('TestID:',
            validators = [
                DataRequired()
                ])
    submit = SubmitField('Delete Test')
