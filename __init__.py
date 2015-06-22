# initialize database
# to initialize db use 'from __init__ import db'

import sys
sys.path.insert(0, '/var/www/html/Charlotte/main/models')


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)				# object that will be our database


import models

'''
import imp
models = imp.load_source('modulename', '/var/www/html/Charlotte/Flask/models/models.py')
'''