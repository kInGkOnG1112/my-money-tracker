import datetime
from extensions import db


# We are creating 3 separate tables - represented by class-based models
# using SQLAlchemy's ORM - each class uses the declarative base from the
# SQLAlchemy model

# Each table will have a unique ID used for the primary key (Integers that
# will auto increment)

# As we are using Flask-SQLAlchemy we don't need to import each column type at
# the top of the file - The db variable contains each of these already - so
# allows us to use dot notation to specify column data types

# Each model also needs a function __repr__ that takes itself as the argument
# It is a standard Python function which stands for
# represent - it means to represent the class objects as a string

# unique=True - makes sure each new data added to the database is unique
# nullable=False - this makes sure that field isn't empty or blank,
# makes it a required field


class Category(db.Model):
    # Schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    icon = db.Column(db.String(200), unique=False, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    icon = db.Column(db.String(200), unique=False, nullable=True)
    balance = db.Column(db.Numeric(10, 2), unique=False, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.name


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    type = db.Column(db.String(10), unique=False, nullable=False)
    amount = db.Column(db.Numeric(10, 2), unique=False, nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id", ondelete="CASCADE"),
        nullable=False)
    account_id = db.Column(
        db.Integer,
        db.ForeignKey("account.id", ondelete="CASCADE"),
        nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.code
