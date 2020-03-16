# moses_app/hospital_stats_summary/views.py

from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_user, login_required, logout_user
import flask_login
from moses_app import db
from moses_app.models import HospitalInfo, Hospitals
from moses_app import models
import datetime
import json
import pandas as pd

hospital_stats_summary_blueprint = Blueprint('hospital_stats_summary', __name__,
                                        template_folder='templates/hospital_stats_summary')

@hospital_stats_summary_blueprint.route('/hospital_stats_summary', methods=['GET', 'POST'])
def hospital_stats_summary():

    sql_query = """
    SELECT
        hospital_name
        , status
        , hospital_address
        , hospital_contact_num

        , num_confirmed_covid
        , num_pui

        , request_supplies
        , num_covid_kits
        , num_face_masks
        , num_surgical_gloves
        , num_alcohol
        , num_face_shield
        , num_hoods
        , num_shoe_covers
        , num_respirators

        , num_doctors_for_covid
        , num_nurses_for_covid
        , num_medstaff_for_covid

        , capacity_quarantine
        , notes

        , hospital_website
        , hospital_email
        , timestamp

    FROM HospitalInfo a
    LEFT JOIN Hospitals b
    ON a.hospital_id = b.id
    """

    table = db.engine.execute(sql_query)
    table = [row for row in table]

    columns = ['Hospital Name', 'Status', 'Address', 'Contact Num',
    'Num Confirmed COVID', 'Num PUI', 'Supplies Requested', 'Num COVID Kits',
    'Num Face Mask', 'Num Surgical Gloves', 'Num Alcohol', 'Num Face Shield',
    'Num Hoods', 'Num Shoe Covers', 'Num Respirators',
    'Num Doctors Assigned', 'Num Nurses Assigned', 'Num Med Staff Assigned',
    'Capacity to Quarantine', 'Notes',
    'Website',  'Email', 'Last Updated']

    df = pd.DataFrame(table)
    print(len(columns))
    print(df.shape)
    df.columns = columns


    df = df.groupby(by='Hospital Name').last().T.reset_index(drop=False)
    df.rename(columns={'index':'Hospital Name'}, inplace=True)
    df = df.T.reset_index().T

    num_cols = len(df.columns)
    df.columns = range(num_cols)
    df.to_csv('table.csv')

    table = df.to_dict()
    table = [{str(k):str(list(v.values())[i]) for k,v in table.items()} for i in range(len(df))]
    hospital_tables = table

    return render_template('hospital_stats_summary.html',
                    hospital_tables=json.dumps(hospital_tables),
                    num_cols=num_cols)
