"""
Application entry point
"""
from app import blueprint
from app.src import create_app
from flask_cors import CORS
from flask_script import Manager

import os
import unittest


app = create_app(os.getenv("FLASK_ENV") or "development")
app.register_blueprint(blueprint)
CORS(app, resources={"/ping/*": {"origins": "*"}})
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
