import os
import json
from app import create_app, sqlalchemy as db
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig
from models import initialize_db
import unittest


class TicketsTestCase(unittest.TestCase):
    """This class represents the Event App test case"""

    def setUp(self):
        """Executed before each test.
         Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client

        self.ticket = {
            "event_id": 2,
            "price": 500,
            "quantity": 50
        }
        self.update_ticket = {
            "event_id": 2,
            "price": 500,
            "quantity": 10
        }

        with self.app.app_context():
            db.create_all()
            initialize_db()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    """
    ============================================
    Tests for Tickets
    ============================================
    """

    def test_create_ticket(self):
        """Test create new tickets endpoint """
        res = self.client().post("/api/v1/events/tickets", json=self.ticket)
        self.assertEqual(res.status_code, 200)

    def test_invalid_create_ticket(self):
        """ Test for invalid ticket id"""
        res = self.client().post("/api/v1/events/tickets",
                                 json={"invalid": "json"})
        self.assertEqual(res.status_code, 400)

    def test_get_ticket(self):
        """Test successfully get a ticket """
        res = self.client().get("/api/v1/events/tickets/1")
        self.assertEqual(res.status_code, 200)

    def test_get_ticket(self):
        """Test successfully get a ticket """
        res = self.client().patch("/api/v1/events/tickets/1",
                                  json=self.update_ticket)
        self.assertEqual(res.status_code, 200)

    def test_get_ticket_404(self):
        """ Test for invalid ticket id"""
        res = self.client().get("/api/v1/events/tickets/100")
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
