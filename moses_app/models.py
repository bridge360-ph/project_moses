# MODELS.PY

# set up db inside __init__.py under app folder
from moses_app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# login manager magic thing
@login_manager.user_loader
def load_user(user_id):
    return Hospitals.query.get(user_id)

# make a table Registration of Hospitals
class Hospitals(db.Model, UserMixin):
    # relationship with HospitalInfo
    # uselist=False means we only return one set of values
    hospitalinfo = db.relationship('HospitalInfo', backref='hospital',
                            uselist = True) #lazy=True

    id = db.Column(db.Integer, primary_key=True) # unique identifier for the row
    hospital_name = db.Column(db.String(64))
    hospital_address = db.Column(db.String(64))
    hospital_website = db.Column(db.String(64))
    hospital_contact_num = db.Column(db.Integer())
    hospital_email = db.Column(db.String(64))

    hospital_user_name = db.Column(db.String(64), unique=True, index=True)
    hospital_pw_hash = db.Column(db.String(128))

    def __init__(self, hospital_name, hospital_address, hospital_website, hospital_contact_num,
                hospital_user_name, hospital_email, password):
        self.hospital_name = hospital_name
        self.hospital_address = hospital_address
        self.hospital_website = hospital_website
        self.hospital_contact_num = hospital_contact_num
        self.hospital_email = hospital_email

        self.hospital_user_name = hospital_user_name
        self.hospital_pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hospital_pw_hash, password)


class HospitalInfo(db.Model):
    __tablename__ = 'hospitalinfo'
    # relationship with registration
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'))

    id = db.Column(db.Integer, primary_key=True) # unique identifier for the row
    timestamp = db.Column(db.String(64))

    num_confirmed_covid = db.Column(db.Integer())
    num_pui = db.Column(db.Integer())

    num_face_masks = db.Column(db.Integer())
    num_covid_kits = db.Column(db.Integer())
    num_respirators = db.Column(db.Integer())

    num_doctors_for_covid = db.Column(db.Integer())
    num_nurses_for_covid = db.Column(db.Integer())
    num_medstaff_for_covid = db.Column(db.Integer())

    capacity_quarantine = db.Column(db.String(64))
    notes = db.Column(db.String())

    def __init__(self, timestamp, hospital_id, num_confirmed_covid, num_pui,
                num_face_masks, num_covid_kits, num_respirators,
                num_doctors_for_covid, num_nurses_for_covid, num_medstaff_for_covid,
                capacity_quarantine, notes):

        self.timestamp = timestamp
        self.hospital_id = hospital_id
        self.num_confirmed_covid = num_confirmed_covid
        self.num_pui = num_pui

        self.num_face_masks = num_face_masks
        self.num_covid_kits = num_covid_kits
        self.num_respirators = num_respirators

        self.num_doctors_for_covid = num_doctors_for_covid
        self.num_nurses_for_covid = num_nurses_for_covid
        self.num_medstaff_for_covid = num_medstaff_for_covid

        self.capacity_quarantine = capacity_quarantine
        self.notes = notes
