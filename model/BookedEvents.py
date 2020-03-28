from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime


class BookedEvent(db.Model):
    __table__ = 'booked_event'
    id = db.Column(db.Integer, primary_key=True, index=True)
    event_id = db.Column(db.Integer, index=True)
    purchaser_id = db.Column(db.Integer, index=True)
    create_at = db.Column(db.Datetime, default=datetime.utcnow(), index=True)
    updated_at = db.Column(db.Datetime, default=datetime.utcnow(), index=True)

    def __repr__(self):
        return f"<BookedEvents {self.id} {self.purchaser_id} {self.event_id}>"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "purchaser_id": self.purchaser_id,
            "created_at": self.create_at,
            "updated_at": self.updated_at
        }
