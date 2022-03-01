from flask import Flask
from flask import current_app


app = Flask(__name__)

from app import views