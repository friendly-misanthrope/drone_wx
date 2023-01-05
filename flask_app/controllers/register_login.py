from flask_app.models import pilot, drone
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import redirect, session, render_template, request

@app.route('/')
def landing_page():
    if 'pilot_id' not in session:
        return render_template('landing_page.html')
    return render_template('dashboard.html')

@app.route('/signup', methods=['POST'])
def submit_registration():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "conf_pass": request.form['conf_pass']
    }

    print(data)
        
    # Don't forget to change to dashboard when dashboard page is ready
    return redirect('/')