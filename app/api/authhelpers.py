from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, decode_token
)
from flask import request, jsonify, url_for, abort
from models import Users
from app.api import api
from functools import wraps


def auth_decorator(role):
    def is_auth(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = Users.query.filter_by(id=user_id).first()
            """if user.role.name is not role:
                return jsonify({"error": user.role.name}), 401
            else:
                return func(*args, **kwargs)"""
        return wrapper
    return is_auth
