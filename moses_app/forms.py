# forms.py under registration

from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, IntegerField, SubmitField)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, email, EqualTo, Optional
from wtforms import ValidationError

class LoginForm(FlaskForm):
    hospital_user_name = StringField('Hospital Username', validators = [DataRequired(message="Required")])
    password = PasswordField("Password", validators=[DataRequired(message="Required")])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    hospital_name = StringField("Hospital Name", validators = [DataRequired(message="Required")])
    hospital_address = StringField("Address", validators = [DataRequired(message="Required")])
    hospital_website = StringField("Website", validators=[Optional()])
    hospital_contact_num = StringField("Contact Number", validators=[Optional()])
    hospital_email = StringField("Email", validators=[DataRequired(message="Required"), email()])

    hospital_user_name = StringField("Username", validators=[DataRequired(message="Required")])
    password = PasswordField("Password", validators=[DataRequired(message="Required"),
                EqualTo('password_confirm', message='Passwords must match!')])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_hospital_email(self, field):
        if User.query.filterby(hospital_email=field.data).first():
            raise ValidationError('Your Hospital Email has been already registered!')

    def check_username(self, field):
        if User.query.filterby(hospital_user_name=field.data).first():
            raise ValidationError('Username is taken!')
