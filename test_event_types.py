import os
import json
from app import create_app, sqlalchemy as db
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig
from models import initialize_db
import unittest


class EventTypesTestCase(unittest.TestCase):
    """This class represents the Event App test case"""

    def setUp(self):
        """Executed before each test.
         Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client

        self.event_t = {
            "name": "Python Tech",
            "description": "Event for python developers all over the world"
        }

        with self.app.app_context():
            db.create_all()
            initialize_db()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    """
    ===========================================
    Event Types Tests
    ===========================================
    """

    def test_create_event_type(self):
        res = self.client().post("/api/v1/events/types", json=self.event_t)
        self.assertEqual(res.status_code, 200)

    def test_update_event_type(self):
        """
        Test Update single event_type success
        """
        res = self.client().patch("/api/v1/events/types/2",
                                  json=self.event_t)
        self.assertEqual(res.status_code, 200)

    def test_get_event_type(self):
        """
        Test get single event_type success
        """
        res = self.client().get("/api/v1/events/types/2")
        self.assertEqual(res.status_code, 200)

    def test_get_all_event_types(self):
        """
        Test get all event_type success and return corresponding data type
        """
        res = self.client().get("/api/v1/events/types")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json["data"], list)
        self.assertGreater(len(res.json["data"]), 0)

    def test_delete_event_type(self):
        """
        Test delete event_type success
        """
        res = self.client().delete("/api/v1/events/types/1")
        self.assertEqual(res.status_code, 200)

    def test_create_event_type_invalid(self):
        res = self.client().post("/api/v1/events/types",
                                 json={"not": "any"})
        self.assertEqual(res.status_code, 400)

    def test_event_type_not_found(self):
        """
        Test get event_type failure with not found error
        """
        res = self.client().get("/api/v1/events/types/100")
        self.assertEqual(res.status_code, 404)

    def test_delete_event_type_not_found(self):
        """
        Test delete event_type failure with not found error
        """
        res = self.client().delete("/api/v1/events/types/150")
        self.assertEqual(res.status_code, 404)

    def test_update_type_not_found(self):
        """
        Test Update event_type failure with not found error
        """
        res = self.client().patch("/api/v1/events/types/99",
                                  json=self.event_t)
        self.assertEqual(res.status_code, 404)

    """def test_create_event_type_unauthorized(self):
        res = self.client().post("/api/v1/events/types",
                                 json=self.event_t)
        self.assertEqual(res.status_code, 401)"""


if __name__ == "__main__":
    unittest.main()
