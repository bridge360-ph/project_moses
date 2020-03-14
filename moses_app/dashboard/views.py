# moses_app/dashboard/views.py

from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_user, login_required, logout_user
import flask_login
from moses_app import db
from moses_app.models import HospitalInfo, Hospitals
from moses_app import models
import datetime
import pandas as pd

dashboard_blueprint = Blueprint('dashboard', __name__,
                                        template_folder='templates/dashboard')

@dashboard_blueprint.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    sql_query = """
    SELECT
        hospital_name
        , hospital_address
        , hospital_website
        , hospital_contact_num
        , hospital_email
        , num_confirmed_covid
        , num_pui
        , num_face_masks
        , num_covid_kits
        , num_respirators
        , num_doctors_for_covid
        , num_nurses_for_covid
        , num_medstaff_for_covid
        , capacity_quarantine
        , notes
        , timestamp
    FROM HospitalInfo a
    LEFT JOIN Hospitals b
    ON a.hospital_id = b.id
    """

    table = db.engine.execute(sql_query)
    table = [row for row in table]

    # df = pd.DataFrame(table, columns=['hospital_name', 'hospital_address',
    #         'hospital_website', 'hospital_contact_num', 'hospital_email',
    #         'num_confirmed_covid', 'num_pui', 'num_face_masks', 'num_covid_kits',
    #         'num_respirators', 'num_doctors_for_covid', 'num_nurses_for_covid',
    #         'num_medstaff_for_covid', 'capacity_quarantine', 'notes',
    #         'timestamp'])

    df = pd.DataFrame(table, columns=['Hospital Name', 'Address',
            'Website', 'Contact Num', 'Email',
            'Num Confirmed COVID', 'Num PUI', 'Num Face Mask', 'Num COVID Kits',
            'Num Respirators', 'Num Doctors Handling', 'Num Nurses Handling',
            'Num Med Staff Handling', 'Capacity to Quarantine', 'Notes',
            'Last Updated'])

    df = df.groupby(by='Hospital Name').last().reset_index(drop=False)
    df.to_html('moses_app/templates/table.html')

    table = df.to_dict()
    # table = {k:list(v.values())[0] for k,v in table.items() }
    hospital_tables = table

    return render_template('dashboard.html', hospital_tables=hospital_tables)
