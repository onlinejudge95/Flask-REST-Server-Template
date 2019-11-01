"""
Application entry point
"""
import os

from flask_cors import CORS

from app import blueprint
from app.src import create_app


app = create_app(os.getenv("FLASK_ENV") or "development")
app.register_blueprint(blueprint)
CORS(app, resources={"/ping/*": {"origins": "*"}})
app.app_context().push()


if __name__ == "__main__":
    app.run()
