from decouple import config

DATABASE_URI = config('DATABASE_URL')

if DATABASE_URI.startswith('postgres'):
	DATABASE_URI = DATABASE_URI.replace('postgres', 'postgresql')

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config('SECRET_KEY', default='this-is-a-secret-key')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True