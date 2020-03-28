from app import sqlalchemy as db, create_app
from json import JSONEncoder
from datetime import datetime
# from passlib.apps import custom_app_context as password_context
# from itsdangerous import TimedJSONWebSignatureSerializer as serializer


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, index=True, default=datetime.now)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # favorite_events = db.Column(db.ARRAY(db.String()))

    """def get_reset_token(self, expires_sec=3000):
        url_serializer = serializer(os.environ['SECRET_KEY'], expires_sec)
        uid = JSONEncoder().encode(self.id)
        return url_serializer.dumps({'user_id': uid}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        url_serializer = serializer(os.environ['SECRET_KEY'])
        try:
            user_id = url_serializer.loads(token)['user_id'].strip(r"\"")
            print(user_id)
        except:
            return None
        user = User.objects(id=user_id).first()
        return user"""

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
