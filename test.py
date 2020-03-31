import os
import json
from app import create_app, sqlalchemy as db
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig
from models import Events, Tickets, EventType
import unittest


class EventAppTestCase(unittest.TestCase):
    """This class represents the Event App test case"""

    def setUp(self):
        """Executed before each test.
         Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
        self.event = {
            "title": "Markup Start",
            "description": "This is an event I am creating for meeting with ",
            "start_datetime": "2020-05-30 15:45",
            "location": "Douala Bonamoussadi",
            "price": 2000,
            "event_type_id": 1
        }

        self.event_t = {
            "name": "Python Tech",
            "description": "Event for python developers all over the world"
        }

        self.ticket = {
            "event_id": 1,
            "email": "chetat@gmail.com"
        }

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        pass

    """
    ===========================================
    Event Types Tests
    ===========================================
    """

    def test_create_event_type(self):
        res = self.client().post("api/v1/events/types", json=self.event_t)
        self.assertEqual(res.status_code, 200)

    def test_create_event_type_fail(self):
        res = self.client().post("api/v1/events/types", json={"not": "any"})
        self.assertEqual(res.status_code, 400)

    def test_get_event_type(self):
        res = self.client().get(f"api/v1/events/types/1")
        self.assertEqual(res.status_code, 200)

    def test_event_type_not_found(self):
        res = self.client().get(f"api/v1/events/types/100")
        self.assertEqual(res.status_code, 404)

    def test_get_all_event_types(self):
        res = self.client().get("api/v1/events/types")
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.json["data"]), 0)

    def test_update_event_type(self):
        res = self.client().patch(f"api/v1/events/types/1")
        self.assertEqual(res.status_code, 200)

    def test_update_type_not_found(self):
        res = self.client().patch("api/v1/events/types/99", json=self.event_t)
        print(res.json)
        self.assertEqual(res.status_code, 404)

    """
    ===========================================
    Events Tests
    ===========================================
    """

    def test_create_new_events(self):
        """Test create new events endpoint """
        res = self.client().post('api/v1/events', json=self.event)
        self.assertEqual(res.status_code, 200)

    def test_failed_create_new_event(self):
        res = self.client().post('api/v1/events', json={"empty": "body"})
        self.assertEqual(res.status_code, 400)

    def test_get_event(self):
        res = self.client().get("api/v1/events/1")
        self.assertEqual(res.status_code, 200)

    def test_get_event_not_found(self):
        res = self.client().patch('api/v1/events/100', json=self.event)
        self.assertEqual(res.status_code, 404)

    def test_update_event(self):
        """Test update event """
        res = self.client().patch('api/v1/events/1', json=self.event)
        self.assertEqual(res.status_code, 200)

    def test_update_event_not_found(self):
        res = self.client().patch('api/v1/events/100', json=self.event)
        self.assertEqual(res.status_code, 404)

    def test_get_all_events(self):
        """Test get all events endpoint """
        res = self.client().get('api/v1/events')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['success'], True)

    """
    ============================================
    Tests for Tickets
    ============================================
    """

    def test_create_ticket(self):
        """Test create new events endpoint """
        res = self.client().post('api/v1/events/tickets', json=self.ticket)
        print(res.json)
        self.assertEqual(res.status_code, 200)

    def test_get_ticket(self):
        """Test create new events endpoint """
        res = self.client().get('api/v1/events/tickets/1')
        self.assertEqual(res.status_code, 200)

    def test_get_ticket_404(self):
        """ Test for invalid ticket id"""
        res = self.client().get(f"api/v1/events/tickets/100")
        self.assertEqual(res.status_code, 404)

    def test_invalid_create_ticket(self):
        """ Test for invalid ticket id"""
        res = self.client().post(f"api/v1/events/tickets",
                                 json={"invali": "json"})
        self.assertEqual(res.status_code, 400)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
