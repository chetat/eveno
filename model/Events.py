from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime
from model.EventType import EventType
from model.Users import Users

class Events(db.Model):
    __table__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    start_date_time = db.Column(db.DateTime,required=True, index=True, default=datetime.utcnow)
    end_date_time = db.Column(db.DateTime,required=True, index=True, default=datetime.utcnow)
    address_id = db.Column(db.Integer, required=True)
    image = db.Column(db.String())
    organizer_id = db.Column(db.Integer, required=True)
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
            "title":self.title,
            "description": self.description,
            "start_date": self.start_date_time,
            "end_date": self.end_date_time,
            "address_id": self.address_id,
            "image_url": self.image,
            "organizer_id": self.organizer_id,
            "price": self.price,
            "event_type":  event_type.name
        }