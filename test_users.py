import os
import json
from app import create_app, sqlalchemy as db
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig
from models import initialize_db
import unittest


class AppTestCase(unittest.TestCase):
    """This class represents the Event App test case"""

    def setUp(self):
        """Executed before each test.
         Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
        print("Hello")
        self.user = {
            "email": "yekuwilfred@gmail.com",
            "firstname": "Yeku Wilfred",
            "lastname": "chetat",
            "phone": "671357962",
            "password": "weezybaby"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            initialize_db()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        res = self.client().post("api/v1/users", json=self.user)
        self.assertTrue(res.status_code, 200)

    def test_get_users(self):
        res = self.client().get("api/v1/users")
        self.assertTrue(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
