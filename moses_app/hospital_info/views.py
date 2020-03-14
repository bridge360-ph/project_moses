# moses_app/hospital_info/views.py

from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_user, login_required, logout_user
import flask_login
from moses_app import db
from moses_app.models import HospitalInfo, Hospitals
from moses_app.hospital_info.forms import HospitalInfoForm
import datetime

hospital_info_blueprint = Blueprint('hospital_info', __name__,
                                        template_folder='templates/hospital_info')

@hospital_info_blueprint.route('/hospital_info', methods=['GET', 'POST'])
@login_required
def hospital_info():
    form = HospitalInfoForm()
    timestamp = datetime.datetime.now()
    hospital_id = flask_login.current_user.id
    hospital_name = flask_login.current_user.hospital_name
    print(hospital_id)

    print("OK0")

    print(form.validate_on_submit())
    if form.validate_on_submit():
        timestamp = datetime.datetime.now()
        print("OKA")

        num_confirmed_covid = form.num_confirmed_covid.data
        num_pui = form.num_pui.data

        print(num_confirmed_covid)

        num_face_masks = form.num_face_masks.data
        num_covid_kits = form.num_covid_kits.data
        num_respirators = form.num_respirators.data

        num_doctors_for_covid = form.num_doctors_for_covid.data
        num_nurses_for_covid = form.num_nurses_for_covid.data
        num_medstaff_for_covid = form.num_medstaff_for_covid.data

        capacity_quarantine = form.capacity_quarantine.data
        notes = form.notes.data

        print("OK1")

        # get new registration entry for database
        new_Application = HospitalInfo(timestamp, hospital_id, num_confirmed_covid, num_pui,
                    num_face_masks, num_covid_kits, num_respirators,
                    num_doctors_for_covid, num_nurses_for_covid, num_medstaff_for_covid,
                    capacity_quarantine, notes)

        print("OK2")
        # add to database
        db.session.add(new_Application)
        db.session.commit()

        print("COMMITTED")

        # return redirect(url_for('hospital_info.hospital_info'))
        return redirect(url_for('dashboard.dashboard'))
    print(form.errors)
    return render_template('hospital_info.html', form=form, timestamp=timestamp,
                            hospital_name=hospital_name)
