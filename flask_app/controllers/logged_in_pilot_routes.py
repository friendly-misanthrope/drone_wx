from flask_app.models import pilot, drone
from flask_app import app
from flask import redirect, session, render_template, request

@app.route('/dashboard')
def display_dashboard():
    if 'pilot_id' in session:
        return render_template('dashboard.html',
        current_pilot = pilot.Pilot.get_by_id(
            {'id': session['pilot_id']}
            ))
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')