# forms.py for applicant info

from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField)
from wtforms.fields.html5 import DateField

class PatientInfoForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    middle_name = StringField("Middle Name")
    suffix = StringField("Suffix")
    date_of_birth = StringField("Date of Birth")
    civil_status = StringField("Civil Status")
    gender = StringField("Gender")
    citizenship = StringField("Citizenship")
    place_of_birth = StringField("Place of Birth")
    home_address = StringField("Home Address")
    city_of_residence = StringField("City of Residence")
    spouse_last_name = StringField("Spouse Last Name")
    spouse_first_name = StringField("Spouse First Name")
    spouse_middle_name = StringField("Spouse Middle Name")
    spouse_suffix = StringField("Suffix")
    submit = SubmitField('Submit')
