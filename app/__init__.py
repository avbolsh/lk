from flask import Flask
from app.config import Config
from .extension import db, migrate, login
import app.models

login.login_view = "auth.login"

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Register blueprints here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, static_folder="static", url_prefix="/auth/")


    return app