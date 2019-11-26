from app import sqlalchemy as db, create_app
from datetime import datetime


class Users(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False,unique=True)
    phone = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, index=True, default=datetime.now)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
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
