from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import timedelta
from app.api import api
from models import Users
from flask import request, jsonify, url_for, abort, render_template, redirect
from Exceptions import (NotFound, BadRequest, UnAuthorized,
                        InternalServerError, Forbiden, MethodNotAllowed)
from flask_jwt_extended import (
    JWTManager, jwt_required,
    create_access_token,
    get_jwt_identity
)


@api.errorhandler(NotFound)
@api.errorhandler(InternalServerError)
@api.errorhandler(BadRequest)
@api.errorhandler(Forbiden)
@api.errorhandler(UnAuthorized)
@api.errorhandler(MethodNotAllowed)
def api_error(error):
    """Catch exceptions globally and serialize into JSON"""
    payload = dict(error.payload or ())
    payload['status'] = error.status_code
    payload['message'] = error.message
    return jsonify(payload), error.status_code


@api.route("/auth", methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not login or not password:
        raise BadRequest("Missing login or password")

    try:
        user = Users.query.filter_by(email=email).first()
    except Exception as e:
        print(e)
        raise InternalServerError("Problem retrieving user")

    if not user:
        raise NotFound(f"User with email {email} not found")
    else:
        user_id = user.serialize.get("id")
        access_token = create_access_token(identity=user_id,
                                           expires_delta=timedelta(hours=24))
        return jsonify({
            "success": True,
            "data": {
                "access_token": access_token,
                "user_id": user_id
            }

        })
