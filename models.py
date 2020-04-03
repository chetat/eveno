from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime


class EventType(db.Model):
    __tablename__ = 'event_type'
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
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.create_at,
            "updated_at": self.updated_at
        }


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    start_date_time = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)
    address = db.Column(db.String())
    image = db.Column(db.String())
    price = db.Column(db.Float)
    event_type_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<Events {self.id} {self.title}>"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date_time,
            "address": self.address,
            "image_url": self.image,
            "price": self.price,
            "event_type_id": self.event_type_id
        }


class Tickets(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True, index=True)
    event_id = db.Column(db.Integer)
    attender_email = db.Column(db.String())
    create_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)

    def __repr__(self):
        return f"<Ticket {self.id} {self.event_id}> "

    @property
    def serialize(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "attender_email": self.attender_email,
            "created_at": self.create_at,
            "updated_at": self.updated_at
        }
