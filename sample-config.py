import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
from pathlib import Path

load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # below points to sqlite database or creates it if it doesn't exist
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DATABASE_URI_HOLDINGS = 'postgresql//postgres:postgres@localhost:5432/make_your_own_db'

