from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import drone
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mydb = "drone_wx"

class Pilot:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.is_certified = False
        self.drones = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = '''
        INSERT INTO pilots
        (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        '''
        return connectToMySQL(mydb).query_db(query)

    @classmethod
    def get_by_id(cls, data):
        query = '''
        SELECT * FROM pilots
        WHERE id = %(id)s;
        '''
        results = connectToMySQL(mydb).query_db(query)
        return cls(results[0])

    @classmethod
    def get_by_email(cls, data):
        query = '''
        SELECT * FROM pilots
        WHERE email = %(email)s;
        '''
        results = connectToMySQL(mydb).query_db(query)
        if len(results) < 1:
            return False
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
        WHERE id = %(id)s;
        '''
        return connectToMySQL(mydb).query_db(query)

    @classmethod
    def get_pilot_with_drones(cls, data):
        pass


    # ----- VALIDATIONS -----
    @classmethod
    def validate_create_pilot(cls, pilot):

        #initialize is_valid to True
        is_valid = True

        # check first name
        if len(pilot['first_name']) < 1:
            flash('First name is required')
            is_valid = False
        elif len(pilot['first_name']) < 3:
            flash('First name must be longer than 2 characters')
            is_valid = False

        # check last name
        if len(pilot['last_name']) < 1:
            flash('last name is required')
            is_valid = False
        elif len(pilot['last_name']) < 3:
            flash('last name must be longer than 2 characters')
            is_valid = False
            
        # check email
        if len(pilot['email']) < 1:
            flash('email is required')
            is_valid = False
        elif not EMAIL_REGEX.match(pilot['email']):
            flash('Invalid E-mail address')
            is_valid = False

        # check password
        if len(pilot['password']) < 1:
            flash('Password is required')
            is_valid = False
        elif len(pilot['password']) < 9:
            flash('Password must be longer than 8 characters')
            is_valid = False

        # check conf_pass valid and == password
        if len(pilot['conf_pass']) < 1:
            flash('Password confimration required')
            is_valid = False
        if pilot['password'] != pilot['conf_pass']:
            flash('Passwords must match')
            is_valid = False
        
        # make sure pilot doesn't already exist
        all_pilots = cls.get_all()
        for this_pilot in all_pilots:
            if this_pilot.email == pilot['email']:
                flash('User already exists!')
                is_valid = False
        
        print(f'Is valid: {is_valid}')
        return is_valid

        