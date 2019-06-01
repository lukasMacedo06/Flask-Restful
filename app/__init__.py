from flask import Flask
from flask_cors import CORS

from app.config import configure_app


app = Flask(__name__)

CORS(app)

configure_app(app)
