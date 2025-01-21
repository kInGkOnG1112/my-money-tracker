import os
import configparser

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ^ Importing all the libraries and modules dependencies

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
config = configparser.RawConfigParser()
config_path = os.path.join(PROJECT_ROOT, 'dev.config')

with open(config_path, 'r') as config_file:
    config.read_file(config_file)

# ^ Locate the root/path of the project
# and check and open the dev.config file
# This file contains all configuration needed

app = Flask(__name__)
# ^ Initialize the application

# Define all the configuration
app.config["SECRET_KEY"] = config.get('config-settings', 'secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('config-settings', 'db_uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('config-settings', 'db_track_modifications')


# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

