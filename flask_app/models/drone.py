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
    def create(cls):
        query = '''
        INSERT INTO drones (manufacturer, model, wind_resistance, precip_ok, high_temp, low_temp)
        VALUES (%(manufacturer)s, %(model)s, %(wind_resistance)s, %(precip_ok)s, %(high_temp)s, %(low_temp)s)
        '''
        return connectToMySQL(mydb).query_db(query)

    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * FROM drones
        WHERE id = %(id)s
        '''
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0])
