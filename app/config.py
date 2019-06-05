import os
from flask.json import jsonify
from exceptions import NotFoundError

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:mamae0@localhost/multicanal'
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:mamae0@localhost/multicanal'

config = {
    'dev': 'app.config.DevelopmentConfig',
    'prod': 'app.config.ProductionConfig'
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'dev')
    app.config.from_object(config[config_name])

def exception_handling(app):
    @app.errorhandler(404)
    def route_not_found(error):
        return jsonify(NotFoundError('Route not found').to_dict()), error.code
