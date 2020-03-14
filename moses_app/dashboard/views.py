# views.py for showing data

# moses_app/registration/views.py

from flask import Blueprint, render_template, redirect, url_for, session
from moses_app import db
from moses_app import models

data_blueprint = Blueprint('data', __name__, template_folder='templates/data')

@data_blueprint.route('/data', methods=['GET', 'POST'])
def data():
    reg_data = models.Hospitals.query.all()
    app_info = models.PatientInfo.query.all()

    id = session.get('reg_id', None)
    print(id)

    user_reg_data = models.Hospitals.query.filter_by(id=id).first()
    user_app_info = models.PatientInfo.query.filter_by(reg_id=id).first()

    return render_template('data.html', reg_data=reg_data, app_info=app_info,
                    user_reg_data=user_reg_data, user_app_info=user_app_info)
