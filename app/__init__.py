"""
Initializes the Flask app and sets up the database with SQLAlchemy.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import text

from .database import Base, engine

from .routes import all_blueprints

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("app.config")

    # Set up logging
    if not app.debug:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/acm_education.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info("ACM Education startup")

    # Register blueprints
    for bp in all_blueprints:
        app.register_blueprint(bp, url_prefix="/api" if bp.name != "main_bp" else "/")


    # Create tables
    with app.app_context():
        with engine.connect() as conn:
            # Disable foreign key checks and drop all tables
            conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
            # Drop other tables as needed
            conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))
            conn.commit()
            
            # Create all tables fresh
            Base.metadata.create_all(bind=engine)

    return app
