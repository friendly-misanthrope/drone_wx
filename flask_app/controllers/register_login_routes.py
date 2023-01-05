from flask_app.models import pilot, drone
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import redirect, session, render_template, request

@app.route('/')
def landing_page():
    if 'pilot_id' in session:
        return redirect('/dashboard')
    return render_template('landing_page.html')

@app.route('/signup', methods=['POST'])
def submit_registration():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "conf_pass": request.form['conf_pass']
    }
    
    # Validate user registration input
    if pilot.Pilot.validate_create_pilot(data):
        # Hash password
        pw_hash = bcrypt.generate_password_hash(data['password'])
        # re-assign data dictionary's password field to newly generated hash
        data['password'] = pw_hash
        # Create pilot object, log new pilot in via Session
        session['pilot_id'] = pilot.Pilot.create(data)
        return redirect('/dashboard')
    return redirect ('/')