from flask_app import app
from flask_app.models import drone, pilot
from flask_app.controllers import register_login_routes, logged_in_pilot_routes

if __name__ == "__main__":
    app.run(debug=True)