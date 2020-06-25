from app.api import api
from flask import jsonify, request
from datetime import datetime, timedelta
from models import Users
from app import sqlalchemy as db
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)
from flask_bcrypt import generate_password_hash, check_password_hash
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource,\
    BadRequest, AuthError


@api.errorhandler(NotFound)
@api.errorhandler(Forbiden)
@api.errorhandler(MethodNotAllowed)
@api.errorhandler(InternalServerError)
def api_error(error):
    payload = dict(error.payload or ())
    payload['code'] = error.status_code
    payload['message'] = error.message
    payload['success'] = error.success
    return jsonify(payload), error.status_code


@api.route("/users", methods=["POST"])
def new_user():
    if request.method != 'POST':
        return jsonify({"error": "Method not allowed!"})

    firstname = request.json.get("firstname", None)
    lastname = request.json.get("lastname", None)
    email = request.json.get("email", None)
    phone = request.json.get("phone", None)
    password = request.json.get("password", None)

    if not email or not password:
        raise BadRequest("Provide email and password")

    user_exist = Users.query.filter_by(email=email).first()

    if user_exist:
        raise ExistingResource({"error": f"""User with email {email} 
                                          and number {phone} exist!"""})
    else:
        hashed_password = generate_password_hash(password).decode('utf-8')
        user = Users(first_name=firstname,
                     last_name=lastname,
                     email=email, phone=phone,
                     password_hash=hashed_password)

    try:
        Users.insert(user)
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError({"error": "Database commit error.\
    Could not process your request!"})
    access_token = create_access_token(identity=user.id,
                                       expires_delta=timedelta(hours=24))

    return jsonify({"success": True,
                    "data": {
                        "user": user.serialize,
                        "access_token": access_token
                        }
                    }), 201


@api.route("/users", methods=['GET'])
def get_all_users():
    try:
        users = Users.query.all()
    except Exception as e:
        print(e)
        raise InternalServerError({"error":
                                   "Server Error! Could not retrieve users."})

    return jsonify({"success": True,
                    "data": [user.serialize for user in users]})


@api.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = Users.query.filter_by(id=user_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError("Problem retrieving user")

    if not user:
        raise NotFound(f"Could not find user with id {user_id}")

    return jsonify({
        "success": True,
        "data": user.serialize
    })


@api.route("/users/<user_id>", methods=["PATCH"])
def update_user_info(user_id):
    firstname = request.json.get("firstname", None)
    lastname = request.json.get("lastname", None)
    email = request.json.get("email", None)
    phone = request.json.get("phone", None)
    password = request.json.get("password", None)

    user = Users.query.filter_by(id=user_id).first()
    if not user:
        raise NotFound(f"Could not find user with id {user_id}")

    if firstname:
        user.first_name = firstname
    if lastname:
        user.last_name = lastname
    if email:
        user.email = email
    if phone:
        user.phone = phone
    if password:
        hashed_password = generate_password_hash(password).decode('utf-8')
        user.password_hash = hashed_password
    user.updated_at = datetime.utcnow()
    try:
        Users.update(user)
    except Exception as e:
        print(e)
        raise InternalServerError("Problem retrieving user")

    return jsonify({
        "success": True,
        "data": user.serialize
    })
