from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, DateTimeField
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
    dob = DateTimeField('Data of Birth',
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
    dob = DateTimeField('Data of Birth',
            validators = [
                DataRequired()
                ])
    gender = StringField('Gender: M/F',
            validators = [
                DataRequired(),
                Length(min=1, max = 1)
                ])
    license_date = DateTimeField('License Date',
            validators = [
                DataRequired()
                ])
    submit = SubmitField('Add Doctor')
