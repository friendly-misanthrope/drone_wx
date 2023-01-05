from flask_app.models import pilot, drone
from flask_app import app
# from flask_bcrypt import Bcrypt
from flask import redirect, session, render_template, request

@app.route('/dashboard')
def display_dashboard():
    if 'pilot_id' in session:
        return render_template('dashboard.html')
    return redirect('/')

