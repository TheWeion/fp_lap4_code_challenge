from os import environ
from flask import Flask
from flask_cors import CORS

from .database.db import db
from .routes.main import main_routes

# Load environment variables

database_uri = environ.get('DATABASE_URL')

if 'postgres:' in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")

# Set up the app

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)
db.app = app
db.init_app(app)

app.register_blueprint(main_routes)

## Main

if __name__ == "__main__":
    app.run(debug=True)