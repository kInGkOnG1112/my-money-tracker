import os
import configparser
import pytz

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from extensions import db, migrate
from .routes.main import main
from .routes.ajax import ajax
from .models import (
    Category,
    Record,
    Account
)

# ^ Importing all the libraries and modules dependencies


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.RawConfigParser()
config_path = os.path.join(PROJECT_ROOT, 'dev.config')

with open(config_path, 'r') as config_file:
    config.read_file(config_file)

# ^ Locate the root/path of the project
# and check and open the dev.config file
# This file contains all configuration needed


# Initialize app and defining the template and static folder
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Define all the configuration
app.config["SECRET_KEY"] = config.get('config-settings', 'secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('config-settings', 'db_uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('config-settings', 'db_track_modifications')

# Initialize the DB in the app
db.init_app(app)
migrate.init_app(app, db)

# Register all blueprint routes
app.register_blueprint(main)
app.register_blueprint(ajax)

# Initialize Flask-Admin
admin = Admin(app, name='My Admin Panel', template_mode='bootstrap4')

# Add views for models
admin.add_view(ModelView(models.Category, db.session))
admin.add_view(ModelView(models.Record, db.session))
admin.add_view(ModelView(models.Account, db.session))


# Add a custom filter to format datetime
@app.template_filter('datetime')
def datetime_format(value, format='%B, %d, %Y %I:%M %p'):
    if isinstance(value, str):
        value = datetime.fromisoformat(value)  # Parse string to datetime
    if value.tzinfo is None:
        value = pytz.utc.localize(value)

    value = value.astimezone(pytz.timezone('Asia/Manila'))
    return value.strftime(format)


# Add a custom filter to format decimal
@app.template_filter('format_decimal')
def format_decimal(value, precision=2):
    if value is None or value == '':
        return '0.00'

    try:
        # Convert to float, format with specified precision and apply thousands comma
        formatted_value = f"{float(value):,.{precision}f}"
    except (ValueError, TypeError):
        return '0.00'  # In case of invalid value

    return formatted_value
