from app.api import api
from flask import jsonify, request
from models import db, Events, EventType
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource,\
    BadRequest, AuthError
from .authhelpers import requires_auth


@api.errorhandler(NotFound)
@api.errorhandler(Forbiden)
@api.errorhandler(405)
@api.errorhandler(InternalServerError)
def api_error(error):
    payload = dict(error.payload or ())
    payload['code'] = error.status_code
    payload['message'] = error.message
    payload['success'] = error.success
    return jsonify(payload), error.status_code


@api.route("/events", methods=["POST"])
# @requires_auth("create:events")
def new_event():
    title = request.json.get("title")
    description = request.json.get("description")
    event_datetime = request.json.get("start_datetime")
    event_location = request.json.get("location")
    attendance_price = request.json.get("price")
    event_type_id = request.json.get("event_type_id")

    if not title or not description or not event_datetime \
            or not event_location or not event_type_id:
        raise BadRequest("Invalid body parameters")

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
        raise InternalServerError(f"Something went wrong on server: {str(e)}")


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


@api.route("/events/<event_id>")
# @requires_auth("read:events")
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
    title = request.json.get("title")
    description = request.json.get("description")
    event_datetime = request.json.get("start_datetime")
    event_location = request.json.get("location")
    attendance_price = request.json.get("price")
    event_type_id = request.json.get("event_type_id")

    if not title or not description or not event_datetime \
            or not event_location or not event_type_id:
        raise BadRequest("Invalid body parameters")

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
