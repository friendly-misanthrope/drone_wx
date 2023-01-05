from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import drone
from flask import flash
import re

mydb = "drone_wx"

class Pilot:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.is_certified = False
        self.drones = []

    @classmethod
    def create(cls, data):
        query = '''
        INSERT INTO pilots
        (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        '''
        return connectToMySQL(mydb).query_db(query)

    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * FROM pilots
        WHERE id = %(id)s
        '''
        results = connectToMySQL(mydb).query_db(query)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = '''
        SELECT * FROM pilots;
        '''
        results = connectToMySQL(mydb).query_db(query)
        all_pilots = []
        for result in results:
            this_pilot = cls(result)
            all_pilots.append(this_pilot)

        return all_pilots

    # Note to self: Overwriting default value for is_certified may cause DB issues later
    @classmethod
    def edit(cls, data):
        query = '''
        UPDATE pilots
        SET first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s,
        is_certified = %(is_certified)s
        WHERE id = %(id)s
        '''
        return connectToMySQL(mydb).query_db(query)