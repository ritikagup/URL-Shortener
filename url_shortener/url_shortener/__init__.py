from flask import Flask 
import os
from .extensions import db
from .routes import short
basedir = os.path.abspath(os.path.dirname(__file__))
def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)

    app.register_blueprint(short)

    return app

