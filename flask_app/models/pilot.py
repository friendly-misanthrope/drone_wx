from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import drone
from flask import flash
import re

mydb = "drone_wx"