from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pilot
from flask import flash
import re

mydb = "drone_wx"

class Drone:
    def __init__(self, data):
        self.manufacturer = data['manufacturer'],
        self.model = data['model'],
        self.wind_resistance = data['wind_resistance'],
        self.precip_ok = data['precip_ok'],
        self.high_temp = data['high_temp'],
        self.low_temp = data['low_temp'],
        self.pilot = None

    @classmethod
    def get_one():
        pass
