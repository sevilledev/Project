from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from PragmatechApp.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    from PragmatechApp.admin.routes import admin
    from PragmatechApp.user.routes import user

    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app