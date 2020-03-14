# forms.py under registration

from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, IntegerField, SubmitField)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, email, EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    hospital_user_name = StringField('Hospital Username', default="", validators = [DataRequired()])
    password = PasswordField("Password", default="", validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    hospital_name = StringField("Hospital Name", default="Hospital Name")
    hospital_address = StringField("Address")
    hospital_website = StringField("Website")
    hospital_contact_num = IntegerField("Contact Number")
    hospital_email = StringField("Email", validators=[DataRequired(), email()])

    hospital_user_name = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(),
                EqualTo('password_confirm', message='Passwords must match!')])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_hospital_email(self, field):
        if User.query.filterby(hospital_email=field.data).first():
            raise ValidationError('Your Hospital Email has been already registered!')

    def check_username(self, field):
        if User.query.filterby(hospital_user_name=field.data).first():
            raise ValidationError('Username is taken!')
