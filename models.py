from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, index=True, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String(), index=True)
    region = db.Column(db.String(), index=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Address {self.id} {self.city}>"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city": self.city,
            "region": self.region,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class BookedEvent(db.Model):
    __tablename__ = 'booked_event'
    id = db.Column(db.Integer, primary_key=True, index=True)
    event_id = db.Column(db.Integer, index=True)
    purchaser_id = db.Column(db.Integer, index=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)

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


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    start_date_time = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)
    end_date_time = db.Column(
        db.DateTime, index=True, default=datetime.utcnow)
    address_id = db.Column(db.Integer)
    image = db.Column(db.String())
    organizer_id = db.Column(db.Integer)
    price = db.Column(db.Float)
    event_type_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<Events {self.id} {self.title}>"

    @property
    def serialize(self):
        event_type = EventType.query.filter_by(id=self.event_type_id).first()
        organizer = Users.query.filter_by(role=organizer).first()
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date_time,
            "end_date": self.end_date_time,
            "address_id": self.address_id,
            "image_url": self.image,
            "organizer_id": self.organizer_id,
            "price": self.price,
            "event_type":  event_type.name
        }


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


class Tickets(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True, index=True)
    event_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)

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
