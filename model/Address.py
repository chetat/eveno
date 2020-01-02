from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime


class Address(db.Model):
    __table__ = 'address'
    id = db.Column(db.Integer, index=True, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String(), index=True)
    region = db.Column(db.String(), index=True)
    created_at = db.Column(db.Datetime, index=True)
    updated_at = db.Column(db.Datetime, index=True)

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
