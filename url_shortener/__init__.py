from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config
from url_shortener import routes

app = Flask(__name__)
app.config.from_object(config('APP_SETTINGS'))

db = SQLAlchemy(app)
migrate = Migrate(app, db)