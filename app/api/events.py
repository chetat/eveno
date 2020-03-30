from app.api import api
from flask import jsonify, request
from models import db, Events, EventType
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource, AuthError
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


@api.route("/events", methods=["POST"])
# @requires_auth("create:events")
def new_event():
    title = request.get_json()["title"]
    description = request.get_json()["description"]
    event_datetime = request.get_json()["start_datetime"]
    event_location = request.get_json()["location"]
    attendance_price = request.get_json()["price"]
    event_type_id = request.get_json()["event_type_id"]

    try:
        new_event = Events(title=title, description=description,
                           start_date_time=event_datetime,
                           address=event_location,
                           price=attendance_price, event_type_id=event_type_id)
        db.session.add(new_event)
        db.session.commit()
        return jsonify(
                        {
                            "success": True,
                            "data": new_event.serialize
                        }
                    )
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError("Something went wrong on server")


@api.route("/events")
# @requires_auth("read:events")
def retrieve_all_events():
    try:
        events = Events.query.all()
        return jsonify(
            {
              "success": True,
              "data": [event.serialize for event in events]
            })
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events.")


@api.route("/events/<event_id>", methods=["GET"])
#@requires_auth("read:events")
def retrieve_single_event(event_id):
    try:
        event = Events.query.filter_by(id=event_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events.")
    if not event:
        raise NotFound(f"Event with Id = {event_id} not found")
    else:
        return jsonify(
                    {
                        "success": True,
                        "data": event.serialize
                    })


@api.route("/events/<event_id>", methods=["PATCH"])
# @requires_auth("update:events")
def update_event_info(event_id):
    title = request.get_json()["title"]
    description = request.get_json()["description"]
    event_datetime = request.get_json()["start_datetime"]
    event_location = request.get_json()["location"]
    attendance_price = request.get_json()["price"]
    event_type_id = request.get_json()["event_type_id"]

    try:
        event = Events.query.filter_by(id=event_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events.")
    if not event:
        raise NotFound(f"Event with Id = {event_id} not found")
    else:
        event.title = title
        event.description = description
        event.start_date_time = event_datetime
        event.location = event_location
        event.price = attendance_price
        event.event_type_id = event_type_id

        db.session.add(event)
        db.session.commit()
        return jsonify(
                    {
                        "success": True,
                        "data": event.serialize
                    })


@api.route("/events/<event_id>", methods=["DELETE"])
# @requires_auth("delete:events")
def delete_event(event_id):
    try:
        event = Events.query.filter_by(id=event_id).first()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve events.")
    if not event:
        raise NotFound(f"Event with Id {event_id} not found")
    else:
        db.session.delete(event)
        db.session.commit()
        return jsonify(
                    {
                        "success": True,
                        "deleted": event_id,
                    }), 200
