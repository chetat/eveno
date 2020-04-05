import os
import json
from app import create_app, sqlalchemy as db
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig
from models import initialize_db
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

        # Authorization headers
        self.admin_token = {
            "AUTHORIZATION": f"Bearer { os.environ['ADMIN_BEARER_TOKEN'] }"
        }
        self.user_token = {
            "AUTHORIZATION": f"Bearer { os.environ['USER_BEARER_TOKEN'] }"
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

    """
    ===========================================
    Event Types Tests
    ===========================================
    """

    def test_create_event_type(self):
        res = self.client().post("/api/v1/events/types", json=self.event_t,
                                 headers=self.admin_token)
        self.assertEqual(res.status_code, 200)

    def test_update_event_type(self):
        """
        Test Update single event_type success
        """
        res = self.client().patch("/api/v1/events/types/2",
                                  json=self.event_t, headers=self.admin_token)
        self.assertEqual(res.status_code, 200)

    def test_get_event_type(self):
        """
        Test get single event_type success
        """
        res = self.client().get("/api/v1/events/types/2", headers=self.admin_token)
        self.assertEqual(res.status_code, 200)

    def test_get_all_event_types(self):
        """
        Test get all event_type success and return corresponding data type
        """
        res = self.client().get("/api/v1/events/types",
                                headers=self.admin_token)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json["data"], list)
        self.assertGreater(len(res.json["data"]), 0)

    def test_delete_event_type(self):
        """
        Test delete event_type success
        """
        res = self.client().delete("/api/v1/events/types/1",
                                   headers=self.admin_token)
        self.assertEqual(res.status_code, 200)

    def test_create_event_type_invalid(self):
        res = self.client().post("/api/v1/events/types",
                                 json={"not": "any"},
                                 headers=self.admin_token)
        self.assertEqual(res.status_code, 400)

    def test_event_type_not_found(self):
        """
        Test get event_type failure with not found error
        """
        res = self.client().get("/api/v1/events/types/100",
                                headers=self.admin_token)
        self.assertEqual(res.status_code, 404)

    def test_delete_event_type_not_found(self):
        """
        Test delete event_type failure with not found error
        """
        res = self.client().delete("/api/v1/events/types/150",
                                   headers=self.admin_token)
        self.assertEqual(res.status_code, 404)

    def test_update_type_not_found(self):
        """
        Test Update event_type failure with not found error
        """
        res = self.client().patch("/api/v1/events/types/99",
                                  json=self.event_t, headers=self.admin_token)
        self.assertEqual(res.status_code, 404)

    def test_create_event_type_unauthorized(self):
        res = self.client().post("/api/v1/events/types",
                                 json=self.event_t, headers=self.user_token)
        self.assertEqual(res.status_code, 401)

    """
    ===========================================
    Events Tests
    ===========================================
    """

    def test_create_new_events(self):
        """
        Test create new events endpoint
        """
        res = self.client().post("/api/v1/events", json=self.event,
                                 headers=self.user_token)
        self.assertEqual(res.status_code, 200)

    def test_get_event(self):
        """
        Test to get single event with given event ID
        """
        res = self.client().get("/api/v1/events/3", headers=self.user_token)
        self.assertEqual(res.status_code, 200)

    def test_update_event(self):
        """
        Test update event with given event_id
        """
        res = self.client().patch("/api/v1/events/1",
                                  json=self.event, headers=self.user_token)
        self.assertEqual(res.status_code, 200)

    def test_delete_event(self):
        """
        Test for delete event failure with not found id
        """
        res = self.client().delete("/api/v1/events/2",
                                   headers=self.user_token)
        self.assertEqual(res.status_code, 200)

    def test_get_all_events(self):
        """
        Test get all events
        """
        res = self.client().get("/api/v1/events", headers=self.user_token)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json["data"], list)
        self.assertGreater(len(res.json["data"]), 0)
        self.assertEqual(res.json['success'], True)

    def test_failed_create_new_event(self):
        """
        Test for failure during creation of new event
        """
        res = self.client().post("/api/v1/events",
                                 json={"empty": "body"},
                                 headers=self.user_token)
        self.assertEqual(res.status_code, 400)

    def test_get_event_not_found(self):
        """
        Test of non-existent event with given id
        """
        res = self.client().get("/api/v1/events/100",
                                json=self.event, headers=self.user_token)
        self.assertEqual(res.status_code, 404)

    def test_update_event_not_found(self):
        """
        Test for update event failure with not found id
        """
        res = self.client().patch("/api/v1/events/100",
                                  json=self.event, headers=self.user_token)
        self.assertEqual(res.status_code, 404)

    def test_delete_event_not_found(self):
        """
        Test for update event failure with not found id
        """
        res = self.client().delete("/api/v1/events/150",
                                   headers=self.user_token)
        self.assertEqual(res.status_code, 404)

    def test_delete_event_unauthorized(self):
        res = self.client().delete("/api/v1/events/3",
                                   headers=self.admin_token)
        self.assertEqual(res.status_code, 401)
        # Failing

    def test_create_new_events_unauthorized(self):
        """
        Test create new events endpoint
        """
        res = self.client().post("/api/v1/events", json=self.event,
                                 headers=self.admin_token)
        self.assertEqual(res.status_code, 401)

    """
    ============================================
    Tests for Tickets
    ============================================
    """

    def test_create_ticket(self):
        """Test create new tickets endpoint """
        res = self.client().post("/api/v1/events/tickets", json=self.ticket,
                                 headers=self.user_token)
        self.assertEqual(res.status_code, 200)

    def test_invalid_create_ticket(self):
        """ Test for invalid ticket id"""
        res = self.client().post("/api/v1/events/tickets",
                                 json={"invalid": "json"},
                                 headers=self.user_token)
        self.assertEqual(res.status_code, 400)

    def test_get_ticket(self):
        """Test successfully get a ticket """
        res = self.client().get("/api/v1/events/tickets/1",
                                headers=self.user_token)
        self.assertEqual(res.status_code, 200)

    def test_get_ticket_404(self):
        """ Test for invalid ticket id"""
        res = self.client().get("/api/v1/events/tickets/100",
                                headers=self.user_token)
        self.assertEqual(res.status_code, 404)

    def test_create_ticket_unauthorized(self):
        res = self.client().post("/api/v1/events/tickets",
                                 json=self.ticket)
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
