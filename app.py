from moses_app import app, db
from flask import render_template, redirect, request, url_for, flash, abort, session
from flask_login import login_user, login_required, logout_user
from moses_app.models import Hospitals, HospitalInfo
from moses_app import models
from moses_app.forms import LoginForm, RegistrationForm

# below are the backend of each html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('ok0')
    if form.validate_on_submit():
        print('ok1')
        hospital_user_name = form.hospital_user_name.data
        user = Hospitals.query.filter_by(hospital_user_name =hospital_user_name).first()
        if user is not None and user.check_password(form.password.data):
            print('ok2')
            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')
            print(next)
            if next == None or not next[0] == '/':
                print('ok3')
                next = url_for('hospital_info.hospital_info')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    warning = ''
    print('ok0')
    if form.validate_on_submit():
        user = Hospitals(hospital_name = form.hospital_name.data,
                    hospital_address = form.hospital_address.data,
                    hospital_website = form.hospital_website.data,
                    hospital_contact_num = form.hospital_contact_num.data,
                    hospital_user_name = form.hospital_user_name.data,
                    hospital_email = form.hospital_email.data,
                    password = form.password.data)

        print('ok1')
        count_user_name = Hospitals.query.filter_by(hospital_user_name=form.hospital_user_name.data).count()
        count_email = Hospitals.query.filter_by(hospital_email=form.hospital_email.data).count()
        print('ok2')
        if  count_user_name < 1 and count_email < 1:
            # add to database
            db.session.add(user)
            db.session.commit()

            print('added user')
            flash("Thanks for registration!")

            # go to services if registered
            return redirect(url_for('index'))
        else:
            warning = 'user already in the database'

    return render_template('register.html', form=form, warning=warning)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
