"""
Tests the app.main.config module.
"""
from flask import current_app
from flask_testing import TestCase
from manage import app

import os
import unittest


class TestBaseConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.BaseConfig")
        return app

    def test_app_is_base_config(self):
        self.assertIsNotNone(app.config.get("BASE_DIR"))
        self.assertIsNotNone(app.config.get("SECRET_KEY"))
        self.assertIsNotNone(app.config.get("ENV"))
        self.assertIsNotNone(app.config.get("DEBUG"))

        self.assertFalse(app.config.get("TESTING"))


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertIsNotNone(current_app)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config.get("TESTING"))
        self.assertTrue(app.config.get("JSONIFY_PRETTYPRINT_REGULAR"))


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.src.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config.get("JSONIFY_PRETTYPRINT_REGULAR"))


if __name__ == "__main__":
    unittest.main()
