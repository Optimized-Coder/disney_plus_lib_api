from flask import Flask
from .extensions import db, migrate
from sqlalchemy import text
from .titles import Title

from .routes.api import api

import requests
from bs4 import BeautifulSoup
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.app_context().push()

    app.register_blueprint(api)

    q = Title.query.first()
    print(q.release_year)

    print(q.convert_year_to_decade())


    return app




def add_images():
    # Connect to the database
    conn = sqlite3.connect('instance/data.db')
    c = conn.cursor()

    # Select all records from the data table
    c.execute("SELECT * FROM data")
    rows = c.fetchall()

    # Loop through each record
    counter = 0
    for i, row in enumerate(rows):
        # Extract the movie title from the database
        title = row[1]
        
        # Construct the Google Images search URL
        search_url = 'https://www.google.com/search?q=' + title + ' movie poster&tbm=isch'
        
        # Send a GET request to the search URL
        response = requests.get(search_url)
        
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the URL of the first image result
        image_url = soup.find('img')['src']
        
        # Update the database record with the image URL
        c.execute("UPDATE data SET img_url = ? WHERE id = ?", (image_url, row[0]))
        
        # Increment the counter
        counter += 1
        
        # Print the counter every 10 records
        if counter % 10 == 0:
            print(f"Processed {counter} records so far.")
        
    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

