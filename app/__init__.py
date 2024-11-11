"""
Initializes the Flask app and sets up the database with SQLAlchemy.
"""

import os

from dotenv import load_dotenv
from flask import Flask

from app.config import SQLALCHEMY_DATABASE_URI
from app.database import init_db

from .routes import all_blueprints, main_bp

# Load environment variables
load_dotenv()


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("app.config")

    # Add a secret key (required for sessions)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "admin")

    # Database configuration - use environment variables
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database connection
    init_db(app)

    # Register main blueprint without prefix
    app.register_blueprint(main_bp)

    # Register all other blueprints with API prefix
    for blueprint in [bp for bp in all_blueprints if bp != main_bp]:
        app.register_blueprint(blueprint, url_prefix="/api")

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        # Close the session if it exists
        if hasattr(app, "session"):
            app.session.close()

    return app
