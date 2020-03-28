from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime


class Tickets(db.Model):
    __table__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True, index=True)
    event_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    create_at = db.Column(db.Datetime, default=datetime.utcnow(), index=True)
    updated_at = db.Column(db.Datetime, default=datetime.utcnow(), index=True)

    def __repr__(self):
        return f"<User {self.id} {self.event_id} {self.user_id}>"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "user_id": self.user_id,
            "created_at": self.create_at,
            "updated_at": self.updated_at
        }
