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
    __tablename__ = 'Hospitals'

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
