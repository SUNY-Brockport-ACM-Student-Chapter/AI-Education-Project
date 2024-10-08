"""
This module contains the main routes for the application.

It defines a Flask Blueprint for the main routes and includes functions for
handling the home page and other general-purpose routes.
"""

from flask import Blueprint, current_app, jsonify

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def home():
    """
    Render the home page of the application.

    This route handles GET requests to the root URL and returns a welcome message.

    Returns:
        str: A welcome message for the API.
    """
    current_app.logger.info("Home page accessed")
    return jsonify({"message": "Welcome to the API"}), 200
