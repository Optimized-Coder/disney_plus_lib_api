# core/init.py
from flask import Flask
import os
from os import path
import pandas as pd
import sqlite3
import shutil

from .extensions import db, migrate
from .routes.api import api



def create_app():
    # runs add_data function if data does not exist
    if not path.exists('./instance/data.db'):
        add_data('data.csv')
        print('database added successfully')
        print('-----------------')
    else:
        print('database already exists')
        print('-----------------')
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] \
        = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    print(f'initiated: {db}')
    print('-----------------')
    migrate.init_app(app, db)
    print(f'initiated: {migrate}')
    print('-----------------')

    app.app_context().push()

    app.register_blueprint(api)
    print(f'blueprint registered: {api}')
    print('-----------------')

    return app

def add_data(csv_filename):
# Uses pandas to load data from a csv file to sqlite database
    """
    Adds data from a csv file to a sqlite database.
    """
    conn = sqlite3.connect('data.db')
    print(f'Connected: {conn}')
    print('-----------------')
    df = pd.read_csv(csv_filename)

    # clean data
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()

    # add data to database
    df.to_sql('data', conn, if_exists='replace', index=False)
    print(f'Data added to df: {df}')
    print('-----------------')
    conn.close()
    print(f'Closed: {conn}')
    print('-----------------')

    # creates a directory for the database
    os.mkdir('./instance')

    # moves db into instance folder
    shutil.move('./data.db', './instance/data.db')

    print('Data added to database.')

'''
Title schema {
    id: int
    title: string
    content_type: string (movie / show)
    description:: string
    release_year: int
    age_certification: string
    runtime: int
    genre: string
    production_countries: string
    seasons: int
    imdb_id: string
    imdb_votes: int
    imdb_rating: float
    tmdb_rating: float
    tmdb_score: float
}
'''