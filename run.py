"""
This module is the entry point for the Flask application.

It creates and runs the Flask app, setting up the necessary configurations
and starting the development server when run directly.
"""

from app import create_app

print("Creating Flask app...")
app = create_app()
print("Flask app created successfully!")


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
