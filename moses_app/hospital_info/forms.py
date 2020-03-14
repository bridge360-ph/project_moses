# forms.py for applicant info

from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField, IntegerField)
from wtforms.fields.html5 import DateField

class HospitalInfoForm(FlaskForm):
    num_confirmed_covid = IntegerField("No. of Confirmed COVID Cases", default=0)
    num_pui = IntegerField("No. of Persons Under Investigation", default=0)
    submit = SubmitField('Submit')
