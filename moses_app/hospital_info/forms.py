# forms.py for applicant info

from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField, IntegerField)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, email, EqualTo, Optional
from wtforms import ValidationError

class HospitalInfoForm(FlaskForm):

    num_confirmed_covid = IntegerField("No. of Confirmed COVID Cases*", validators=[Optional()]) #validators=[DataRequired()
    num_pui = IntegerField("No. of Persons Under Investigation*", validators=[Optional()]) #validators=[DataRequired()

    status = SelectField("Hospital Status", default='Unknown', choices=[('Unknown', 'Unknown'),
                                                    ('accepting', 'Accepting COVID Patients'),
                                                    ('not_accepting', 'Not Accepting COVID Patients'),
                                                    ('operating', 'Ongoing Operations'),
                                                     ('stopped', 'Stopped Operations')],
                                                     validators=[Optional()])
    request_supplies = TextAreaField("Request Supplies", validators=[Optional()])
    num_covid_kits = IntegerField("No. of COVID kits", validators=[Optional()])
    num_face_masks = IntegerField("No. of Face Masks", validators=[Optional()])
    num_surgical_gloves = IntegerField("No. of Surgical Gloves", validators=[Optional()])
    num_alcohol = IntegerField("No. of Alcohol", validators=[Optional()])
    num_face_shield = IntegerField("No. of Face Shields", validators=[Optional()])
    num_hoods = IntegerField("No. of Disposable Hoods", validators=[Optional()])
    num_shoe_covers = IntegerField("No. of Shoe Covers", validators=[Optional()])
    num_respirators = IntegerField("No. of Respirators", validators=[Optional()])

    num_doctors_for_covid = IntegerField("No. of Doctors Assigned for COVID", validators=[Optional()])
    num_nurses_for_covid = IntegerField("No. of Nurses Assigned for COVID", validators=[Optional()])
    num_medstaff_for_covid = IntegerField("No. of Medical Staff Assigned For COVID", validators=[Optional()])

    capacity_quarantine = SelectField("Capacity to Quarantine? e.g. Facilities, Staff", default='Unknown', choices=[('Unknown', 'Unknown'), ('Y', 'Yes'), ('N', 'No')], validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField('Submit')
