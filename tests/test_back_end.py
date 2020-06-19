from flask import url_for
from flask_testing import TestCase
from datetime import datetime
from application import app, db
from application.models import Facilities, Patients, Doctors, Tests
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        facility  = Facilities(facility_name="Nightingale", address="Some street", capacity="30")
        patient = Patients(first_name="John", last_name="Doe", dob="01/01/20", gender="M", address="mystreet", telephone="07897452676", email="john@john.com")
        doctor = Doctors(first_name="Nick", last_name="doctor", dob="01/01/20", gender="M", license_date="01/01/20")
        test = Tests(date="01/01/20", outcome='Positive', patient_id="1", facility_id="1", doctor_id="1")

        # save users to database
        db.session.add(facility)
        db.session.add(patient)
        db.session.add(doctor)
        db.session.add(test)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_facility_view(self):
        response = self.client.get(url_for('facilities'))
        self.assertEqual(response.status_code, 200)

    def test_patient_view(self):
        response = self.client.get(url_for('patients'))
        self.assertEqual(response.status_code, 200)

    def test_doctor_view(self):
        response = self.client.get(url_for('doctors'))
        self.assertEqual(response.status_code, 200)

    def test_test_view(self):
        response = self.client.get(url_for('tests'))
        self.assertEqual(response.status_code, 200)
