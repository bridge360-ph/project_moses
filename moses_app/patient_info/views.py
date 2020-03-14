# moses_app/patient_info/views.py

from flask import Blueprint, render_template, redirect, url_for, session
from moses_app import db
from moses_app.models import PatientInfo
from moses_app.patient_info.forms import PatientInfoForm

patient_info_blueprint = Blueprint('patient_info', __name__,
                                        template_folder='templates/patient_info')

@patient_info_blueprint.route('/reg_proc_app_info', methods=['GET', 'POST'])
def reg_proc_app_info():
    form = PatientInfoForm()
    reg_id = session.get('reg_id', None)
    if form.validate_on_submit():
        last_name = form.last_name.data
        first_name = form.first_name.data
        middle_name = form.middle_name.data
        suffix = form.suffix.data
        date_of_birth = form.date_of_birth.data
        civil_status = form.civil_status.data
        gender = form.gender.data
        citizenship = form.citizenship.data
        place_of_birth = form.place_of_birth.data
        home_address = form.home_address.data
        city_of_residence = form.city_of_residence.data
        spouse_last_name = form.spouse_last_name.data
        spouse_first_name = form.spouse_first_name.data
        spouse_middle_name = form.spouse_middle_name.data
        spouse_suffix = form.spouse_suffix.data

        # get new registration entry for database
        new_Application = PatientInfo(reg_id, last_name, first_name,
                    middle_name, suffix, date_of_birth, civil_status, gender,
                    citizenship, place_of_birth, home_address, city_of_residence,
                    spouse_last_name, spouse_first_name, spouse_middle_name,
                    spouse_suffix)

        # add to database
        db.session.add(new_Application)
        db.session.commit()

        return redirect(url_for('data'))

    return render_template('reg_proc_app_info.html', form=form)
