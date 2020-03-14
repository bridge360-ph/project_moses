# moses_app/hospital_info/views.py

from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_user, login_required, logout_user
from moses_app import db
from moses_app.models import HospitalInfo
from moses_app.hospital_info.forms import HospitalInfoForm

hospital_info_blueprint = Blueprint('hospital_info', __name__,
                                        template_folder='templates/hospital_info')

@hospital_info_blueprint.route('/hospital_info', methods=['GET', 'POST'])
@login_required
def hospital_info():
    form = HospitalInfoForm()
    hospital_id = session.get('hospital_id', None)
    if form.validate_on_submit():
        num_confirmed_covid = form.num_confirmed_covid.data
        num_pui = form.num_pui.data

        # get new registration entry for database
        new_Application = HospitalInfo(hospital_id, num_confirmed_covid, num_pui)

        # add to database
        db.session.add(new_Application)
        db.session.commit()

        return redirect(url_for('hospital_info.hospital_info'))

    return render_template('hospital_info.html', form=form)
