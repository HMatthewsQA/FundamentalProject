import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Patients, Doctors, Facilities, Tests

test_patient_first_name = "ATest"
test_patient_last_name = "BTest"
test_patient_dob = "09/10/18"
test_patient_gender = "F"
test_patient_address = "A test street"
test_patient_telephone = "07567123456"
test_patient_email = "test@test.com"


class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
        app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/hmatthews/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestRegistration(TestBase):

    def test_registration(self):

        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("/html/body/form[1]/button").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_patient_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_patient_last_name)
        self.driver.find_element_by_xpath('//*[@id="dob"]').send_keys(test_patient_dob)
        self.driver.find_element_by_xpath('//*[@id="gender"]').send_keys(test_patient_gender)
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(test_patient_address)
        self.driver.find_element_by_xpath('//*[@id="telephone"]').send_keys(test_patient_telephone)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_patient_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('patients') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
