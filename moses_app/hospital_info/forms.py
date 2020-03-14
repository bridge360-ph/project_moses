# forms.py for applicant info

from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField, IntegerField)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, email, EqualTo, Optional
from wtforms import ValidationError

class HospitalInfoForm(FlaskForm):

    num_confirmed_covid = IntegerField("No. of Confirmed COVID Cases*", validators=[DataRequired(message="Required")]) #validators=[DataRequired()
    num_pui = IntegerField("No. of Persons Under Investigation*", validators=[DataRequired(message="Required")]) #validators=[DataRequired()

    num_face_masks = IntegerField("No. of Face Masks", validators=[Optional()])
    num_covid_kits = IntegerField("No. of COVID kits", validators=[Optional()])
    num_respirators = IntegerField("No. of Respirators", validators=[Optional()])

    num_doctors_for_covid = IntegerField("No. of Doctors for COVID", validators=[Optional()])
    num_nurses_for_covid = IntegerField("No. of Nurses for COVID", validators=[Optional()])
    num_medstaff_for_covid = IntegerField("No. of Medical Staff For COVID", validators=[Optional()])

    capacity_quarantine = SelectField("Capacity to Quarantine? e.g. Facilities, Staff", default='Unknown', choices=[('Unknown', 'Unknown'), ('Y', 'Yes'), ('N', 'No')], validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField('Submit')
