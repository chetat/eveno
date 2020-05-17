from app.api import api
from flask import jsonify, request
from models import db, Events, EventType
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


"""
This endpoint creates a new event
:return: returns an event json object
"""
@api.route("/events", methods=["POST"])
def new_event():
    title = request.json.get("title", None)
    description = request.json.get("description", None)
    event_datetime = request.json.get("start_datetime", None)
    event_location = request.json.get("location", None)
    image_url = request.json.get("image_url", None)
    event_type_id = request.json.get("event_type_id", None)
    organizer_id = request.json.get("organizer_id", None)

    if not title or not description or not event_datetime \
            or not event_location or not event_type_id:
        raise BadRequest("Invalid body parameters")

    try:
        new_event = Events(title=title, description=description,
                           start_date_time=event_datetime,
                           event_location=event_location,
                           image=image_url,
                           organizer_id=organizer_id,
                           event_type_id=event_type_id
                           )
        Events.insert(new_event)
        return jsonify(
            {
                "success": True,
                "data": new_event.serialize
            }
        )
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError(f"Something went wrong on server")


"""
This Retrieve all events types
:return: returns a list of event json objects
"""
@api.route("/events")
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


"""
This endpoint get an event with given id
:params event_id: The event Id generated by database
:return: returns an event json object corresponding to the event id
"""
@api.route("/events/<event_id>")
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


"""
This endpoint update an event with given id
:params event_id: The event Id generated by database
:return: returns an event json object corresponding to the event id
"""
@api.route("/events/<event_id>", methods=["PATCH"])
def update_event_info(event_id):
    title = request.json.get("title")
    description = request.json.get("description")
    event_datetime = request.json.get("start_datetime")
    event_location = request.json.get("location")
    attendance_price = request.json.get("price")
    event_type_id = request.json.get("event_type_id")
    image_url = request.json.get("image_url")

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
        event.image_url = image_url

        Events.update(event)
        return jsonify(
            {
                "success": True,
                "data": event.serialize
            })


"""
This endpoint delete an eventwith given id
:params event_id: The event Id generated by databas
:return: returns deleted event Id and success of True
"""
@api.route("/events/<event_id>", methods=["DELETE"])
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
        Events.delete(event)
        return jsonify(
            {
                "success": True,
                "deleted": event_id,
            }), 200
