from app.api import api
from flask import jsonify, request
from models import db, EventType
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource,\
    BadRequest, AuthError
from .authhelpers import requires_auth


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


@api.route("/events/types", methods=["POST"])
# @requires_auth("create:events")
def new_event_type():
    name = request.json.get("name")
    description = request.json.get("description")

    if not name or not description:
        raise BadRequest("Invalid body provided")

    try:
        new_event_type = EventType(name=name, description=description)
        db.session.add(new_event_type)
        db.session.commit()
        return jsonify(new_event_type.serialize)
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError("Could not create event type")


@api.route("/events/types")
# @requires_auth("read:events")
def retrieve_all_events_types():
    try:
        event_types = EventType.query.all()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve users.")

    return jsonify(
        {
            "success": True,
            "data": [event_type.serialize for event_type in event_types]
        }
    )


@api.route("/events/types/<type_id>")
def get_event_type(type_id):
    try:
        event_type = EventType.query.filter_by(id=type_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events types.")
    if not event_type:
        raise NotFound(f"Event with Id {type_id} not found")
    else:
        return jsonify(
            {
                "success": True,
                "data": event_type.serialize
            }
        )


@api.route("/events/types/<type_id>", methods=["PATCH"])
# @requires_auth("update:events")
def update_event_type(type_id):
    name = request.json.get("name")
    description = request.json.get("description")

    if not name or not description:
        raise BadRequest("Invalid body provided")

    try:
        event_type = EventType.query.filter_by(id=type_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events.")
    if not event_type:
        raise NotFound(f"Event with Id = {type_id} not found")
    else:
        event_type.name = name
        event_type.description = description

        db.session.add(event_type)
        db.session.commit()
        return jsonify(
            {
                "success": True,
                "data": event_type.serialize
            })


@api.route("/events/types/<type_id>", methods=["DELETE"])
# @requires_auth("delete:events")
def delete_event_type(type_id):
    try:
        event_type = EventType.query.filter_by(id=type_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events types.")
    if not event_type:
        raise NotFound(f"Event with Id {type_id} not found")
    else:
        db.session.delete(event_type)
        db.session.commit()
        return jsonify(
            {
                "success": True,
                "deleted": type_id,
            }), 200
