from application import db 
from application.models import Facilities, Patients, Doctors, Tests

db.drop_all()
db.create_all()
