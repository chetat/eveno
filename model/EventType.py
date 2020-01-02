from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime

class EventType(db.Model):
    __table__ = 'event_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    create_at = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return f"<EventType {self.id} {self.name}>"

    @property
    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.create_at,
            "updated_at": self.updated_at
        }