from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pilot
from flask import flash
import re

mydb = "drone_wx"

class Drone:
    def __init__(self, data):
        self.manufacturer = data['manufacturer']
        self.model = data['model']
        self.wind_resist_kts = data['wind_resist_kts']
        self.precip_ok = data['precip_ok']
        self.high_temp = data['high_temp']
        self.low_temp = data['low_temp']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pilot = None

    @classmethod
    def create(cls):
        query = '''
        INSERT INTO drones (manufacturer, model, wind_resistance, precip_ok, high_temp, low_temp)
        VALUES (%(manufacturer)s, %(model)s, %(wind_resistance)s, %(precip_ok)s, %(high_temp)s, %(low_temp)s);
        '''
        return connectToMySQL(mydb).query_db(query)

    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * FROM drones
        WHERE id = %(id)s;
        '''
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = '''
        SELECT * FROM drones;
        '''
        results = connectToMySQL(mydb).query_db(query)
        all_drones = []
        for drone in results:
            this_drone = cls(drone)
            all_drones.append(this_drone)
        return all_drones
