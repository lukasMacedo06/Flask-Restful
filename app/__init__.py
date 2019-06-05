import importlib

from flask import Flask
from flask_cors import CORS

from app.config import configure_app, exception_handling
from app.environments import Environments as env


app = Flask(__name__)

CORS(app)

configure_app(app)

exception_handling(app)

for module in env.MODULE:
    for version in range(1,env.VERSION + 1):
        package = importlib.import_module('app.views.v{}'.format(version), package='app')
        app.register_blueprint(
            getattr(package, 'v{}_{}'.format(version, module['bp'])),
            url_prefix='/v{}/{}'.format(version, module['bp'])
        )
