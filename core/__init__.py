from flask import Flask
from os import path
import pandas as pd
import sqlite3

from .extensions import db, migrate
from .titles import Title
from .routes.api import api


def create_app():
    # runs add_data function if data does not exist
    if not path.exists('./instance/data.db'):
        add_data('data.csv')
        print('database added successfully')
    else:
        print('database already exists')
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] \
        = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.app_context().push()

    app.register_blueprint(api)

    return app

def add_data(csv_filename):
# Uses pandas to load data from a csv file to sqlite database
    """
    Adds data from a csv file to a sqlite database.
    """
    conn = sqlite3.connect('data.db')
    df = pd.read_csv(csv_filename)

    # clean data
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()

    df.to_sql('data', conn, if_exists='replace', index=False)
    conn.close()
    print('Data added to database.')


