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


@main_bp.route("/health")
def health_check():
    """
    Check the health status of the application.

    This route provides a simple health check endpoint that returns a 200 status
    code if the application is running properly.

    Returns:
        dict: A JSON response containing the status of the application.
    """
    current_app.logger.debug("Health check performed")
    return (
        jsonify(
            {
                "status": "healthy",
                "service": "API",
                "version": current_app.config.get("VERSION", "1.0.0"),
            }
        ),
        200,
    )


@main_bp.route("/routes")
def list_routes():
    """
    List all available routes in the application.

    This endpoint returns a list of all registered routes in the application,
    including their URL patterns, methods, and endpoint names.

    Returns:
        dict: A JSON response containing all available routes.
    """
    routes = []
    for rule in current_app.url_map.iter_rules():
        # Skip the static endpoint
        if rule.endpoint == "static":
            continue

        methods = sorted(
            [method for method in rule.methods if method not in ["HEAD", "OPTIONS"]]
        )
        routes.append(
            {
                "endpoint": rule.endpoint,
                "methods": methods,
                "url": str(rule),
                "blueprint": (
                    rule.endpoint.split(".")[0] if "." in rule.endpoint else "app"
                ),
            }
        )

    # Sort routes by URL for better readability
    routes = sorted(routes, key=lambda x: x["url"])

    current_app.logger.info("Routes list accessed")
    return (
        jsonify(
            {
                "total_routes": len(routes),
                "routes": routes,
            }
        ),
        200,
    )
