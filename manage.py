"""
Application entry point
"""
import os
import unittest

from flask_cors import CORS
from flask_script import Manager

from app import blueprint
from app.src import create_app


app = create_app(os.getenv("FLASK_ENV") or "development")  # pylint: disable=invalid-name
app.register_blueprint(blueprint)
CORS(app, resources={"/ping/*": {"origins": "*"}})
app.app_context().push()

manager = Manager(app)  # pylint: disable=invalid-name


@manager.command
def run():
    """
    Command to run the server at localhost:5000 for default values.

    $ python manage.py run
    """
    app.run()


@manager.command
def test():
    """
    Runs the unit tests.

    $ python manage.py test
    """
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
