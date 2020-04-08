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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()

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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "attender_email": self.attender_email,
            "created_at": self.create_at,
            "updated_at": self.updated_at
        }


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.String())
    password_hash = db.Column(db.String())
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @property
    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __repr__(self):
        return f"<User {self.id} {self.name}>"


def initialize_db():
    # Initial Events
    event_1 = Events(
        title="Markup Start",
        description="This is an event I am creating for meeting with friends",
        start_date_time="2020-05-30 15:45",
        address="Douala Bonamoussadi",
        price=2000,
        event_type_id=2
    )
    event_2 = Events(
        title="Markup Start",
        description="This is an event I am creating for meeting with friends",
        start_date_time="2020-05-30 15:45",
        address="Douala Makepe",
        price=5000,
        event_type_id=1
    )
    event_3 = Events(
        title="Markup Start",
        description="This is an event I am creating for meeting with friends",
        start_date_time="2020-05-30 15:45",
        address="Douala Bonamoussadi",
        price=2000,
        event_type_id=1
    )

    event_type_1 = EventType(
        name="TechEvent",
        description="An event related to tech talks and Python programming"
    )
    event_type_2 = EventType(
        name="gaming",
        description="An event related Game players and Games"
    )

    ticket_1 = Tickets(
        event_id=1,
        attender_email="yekuwilfred@gmail.com"
    )
    ticket_2 = Tickets(
        event_id=2,
        attender_email="chetat@gmail.com"
    )

    # Create Event types
    EventType.insert(event_type_1)
    EventType.insert(event_type_2)

    # Create new events
    Events.insert(event_1)
    Events.insert(event_2)
    Events.insert(event_3)

    # Create new tickets
    Tickets.insert(ticket_1)
    Tickets.insert(ticket_2)
