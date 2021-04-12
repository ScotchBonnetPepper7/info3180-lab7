from flask import Flask
from app.config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'spicy'
app.config.from_object(Config)

UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views
