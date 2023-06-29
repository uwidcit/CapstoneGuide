import os
import importlib
from datetime import timedelta

# must be updated to inlude addtional secrets/ api keys & use a gitignored custom-config file instad
def load_config():
    config = {'ENV': os.environ.get('ENV', 'DEVELOPMENT')}
    delta = 7
    if config['ENV'] == "DEVELOPMENT":
        from .default_config import JWT_ACCESS_TOKEN_EXPIRES, SQLALCHEMY_DATABASE_URI, SECRET_KEY
        config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        config['SECRET_KEY'] = os.urandom(24)
        # config['GPT_KEY'] = GPT_KEY
        delta = JWT_ACCESS_TOKEN_EXPIRES
        # config["SESSION_PERMANENT"] = False
    else:
        db_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if db_path.startswith("postgres://"):
            db_path = db_path.replace("postgres://","postgresql://", 1) 
        config['SQLALCHEMY_DATABASE_URI'] = db_path
        config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        config['RAWG_TOKEN'] = os.environ.get('RAWG_TOKEN')
        config['GPT_KEY'] = os.environ.get('GPT_KEY')
        config['DEBUG'] = config['ENV'].upper() != 'PRODUCTION'
        delta = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 7))

    config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=int(delta))
    config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config['TEMPLATES_AUTO_RELOAD'] = True
    config['SEVER_NAME'] = '0.0.0.0'
    config['PREFERRED_URL_SCHEME'] = 'https'
    config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    config["JWT_TOKEN_LOCATION"] = ["headers"]
    # config["SESSION_PERMANENT"] = False
    return config

config = load_config()