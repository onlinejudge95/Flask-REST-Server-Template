"""
Tests the app.main.config module.
"""
from flask import current_app
from flask_testing import TestCase

from manage import app



class TestBaseConfig(TestCase):
    """
    Testclass for testing BaseConfig class.
    This class checks if certain basic settings are
    available for the app.

    Following test methods are present

    * test_app_is_base_config

    You need not instantiate this class, the test loader
    will take care of test discovery and pick all modules
    in app/test that begin with `test` string.
    After the modules has been discovered the runner will pick
    up all the classes that inherit from the flask_testing.TestCase
    which is a wrapper around unittest.TestCase.
    After the test classes have been loaded the runner will
    run all methods that start with test_.
    """
    def create_app(self):
        app.config.from_object("app.src.config.BaseConfig")
        return app

    def test_app_is_base_config(self):
        """
        Method to test whether the base config class
        functions perfectly right or not.
        Asserts whether the proper values for the
        defined config are set or not.
        """
        self.assertIsNotNone(app.config.get("BASE_DIR"))
        self.assertIsNotNone(app.config.get("SECRET_KEY"))
        self.assertIsNotNone(app.config.get("ENV"))
        self.assertIsNotNone(app.config.get("DEBUG"))

        self.assertFalse(app.config.get("TESTING"))


class TestDevelopmentConfig(TestCase):
    """
    Testclass for testing DevelopmentConfig class.
    This class checks if certain basic settings are
    available for the app in development environment.

    Following test methods are present

    * test_app_is_development

    You need not instantiate this class, the test loader
    will take care of test discovery and pick all modules
    in app/test that begin with `test` string.
    After the modules has been discovered the runner will pick
    up all the classes that inherit from the flask_testing.TestCase
    which is a wrapper around unittest.TestCase.
    After the test classes have been loaded the runner will
    run all methods that start with test_.
    """
    def create_app(self):
        app.config.from_object("app.src.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        """
        Method to test whether the development
        config class functions perfectly right or not.
        Asserts whether the proper values for the
        defined config are set or not.
        """
        self.assertIsNotNone(current_app)


class TestTestingConfig(TestCase):
    """
    Testclass for testing TestingConfig class.
    This class checks if certain basic settings are
    available for the app in testing environment.

    Following test methods are present

    * test_app_is_testing

    You need not instantiate this class, the test loader
    will take care of test discovery and pick all modules
    in app/test that begin with `test` string.
    After the modules has been discovered the runner will pick
    up all the classes that inherit from the flask_testing.TestCase
    which is a wrapper around unittest.TestCase.
    After the test classes have been loaded the runner will
    run all methods that start with test_.
    """
    def create_app(self):
        app.config.from_object("app.src.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        """
        Method to test whether the test
        config class functions perfectly right or not.
        Asserts whether the proper values for the
        defined config are set or not.
        """
        self.assertTrue(app.config.get("TESTING"))
        self.assertTrue(app.config.get("JSONIFY_PRETTYPRINT_REGULAR"))


class TestProductionConfig(TestCase):
    """
    Testclass for testing ProductionConfig class.
    This class checks if certain basic settings are
    available for the app in production environment.

    Following test methods are present

    * test_app_is_production

    You need not instantiate this class, the test loader
    will take care of test discovery and pick all modules
    in app/test that begin with `test` string.
    After the modules has been discovered the runner will pick
    up all the classes that inherit from the flask_testing.TestCase
    which is a wrapper around unittest.TestCase.
    After the test classes have been loaded the runner will
    run all methods that start with test_.
    """
    def create_app(self):
        app.config.from_object("app.src.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        """
        Method to test whether the production
        config class functions perfectly right or not.
        Asserts whether the proper values for the
        defined config are set or not.
        """
        self.assertTrue(app.config.get("JSONIFY_PRETTYPRINT_REGULAR"))
