import os
import json
from app import create_app, sqlalchemy as db
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig
from models import initialize_db
import unittest


class EventsTestCase(unittest.TestCase):
    """This class represents the Event App test case"""

    def setUp(self):
        """Executed before each test.
         Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client

        self.event = {
            "title": "Markup Start",
            "description": "This is an event I am creating fo\
            r meeting with friends",
            "start_datetime": "2020-05-30 15:45",
            "location": "Douala Bonamoussadi",
            "event_type_id": 1,
            "image_url": "https://img.nen/j.png",
            "organizer_id": 1
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
    Events Tests
    ===========================================
    """

    def test_create_new_events(self):
        """
        Test create new events endpoint
        """
        res = self.client().post("/api/v1/events", json=self.event)
        self.assertEqual(res.status_code, 200)

    def test_get_event(self):
        """
        Test to get single event with given event ID
        """
        res = self.client().get("/api/v1/events/3")
        self.assertEqual(res.status_code, 200)

    def test_update_event(self):
        """
        Test update event with given event_id
        """
        res = self.client().patch("/api/v1/events/1",
                                  json=self.event)
        self.assertEqual(res.status_code, 200)

    def test_delete_event(self):
        """
        Test for delete event failure with not found id
        """
        res = self.client().delete("/api/v1/events/2")
        self.assertEqual(res.status_code, 200)

    def test_get_all_events(self):
        """
        Test get all events
        """
        res = self.client().get("/api/v1/events")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json["data"], list)
        self.assertGreater(len(res.json["data"]), 0)
        self.assertEqual(res.json['success'], True)

    def test_failed_create_new_event(self):
        """
        Test for failure during creation of new event
        """
        res = self.client().post("/api/v1/events",
                                 json={"empty": "body"})
        self.assertEqual(res.status_code, 400)

    def test_get_event_not_found(self):
        """
        Test of non-existent event with given id
        """
        res = self.client().get("/api/v1/events/100",
                                json=self.event)
        self.assertEqual(res.status_code, 404)

    def test_update_event_not_found(self):
        """
        Test for update event failure with not found id
        """
        res = self.client().patch("/api/v1/events/100",
                                  json=self.event)
        self.assertEqual(res.status_code, 404)

    def test_delete_event_not_found(self):
        """
        Test for update event failure with not found id
        """
        res = self.client().delete("/api/v1/events/150")
        self.assertEqual(res.status_code, 404)
        """
            def test_delete_event_unauthorized(self):
                res = self.client().delete("/api/v1/events/3")
                self.assertEqual(res.status_code, 401)
                # Failing"""

    """def test_create_new_events_unauthorized(self):
        # Test create new events endpoint
        res = self.client().post("/api/v1/events", json=self.event)
        self.assertEqual(res.status_code, 401)"""


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
