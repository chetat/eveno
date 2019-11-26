from app.api import api
from flask import jsonify, request
from model.Users import db, Users
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource


@api.errorhandler(NotFound)
@api.errorhandler(Forbiden)
@api.errorhandler(MethodNotAllowed)
@api.errorhandler(InternalServerError)
@api.errorhandler(ExistingResource)
def api_error(error):
    payload = dict(error.payload or ())
    payload['code'] = error.status_code
    payload['message'] = error.message
    payload['success'] = error.success
    return jsonify(payload), error.status_code



@api.route('/users', methods=['POST'])
def new_user():
    """Create new users 
    return: user access token
    """
    if request.method != 'POST':
        raise MethodNotAllowed("Method not allowed!")

    firstname = request.json.get("firstname")
    lastname = request.json.get("lastname")
    email = request.json.get("email")
    phone = request.json.get("phone")

    user_exist = Users.query.filter_by(email=email).first()

    if user_exist:
        raise ExistingResource(f"User with email {email} and number {phone} exist!")

    user = Users(first_name=firstname, last_name=lastname, email=email, phone=phone)
    
    try:
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        raise InternalServerError("Could not process your request!")
    """finally:
        db.session.close()"""  
        #Closing session here will cause errors in testing because it will be prematured

    return jsonify(user.serialize),201


@api.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = Users.query.all()
    except:
        raise InternalServerError("Internal Server Error! Could not retrieve users.")

    return jsonify({"success": True,"data":[user.serialize for user in users]})