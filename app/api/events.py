from app.api import api
from flask import jsonify, request
from model.Users import db, Users
from model.Events import EventType
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


@api.route("/events", methods=["POST"])
def new_event():
    return jsonify({"events":"new events"})


@api.route("/events", methods=["GET"])
def retrieve_all_events():
    return jsonify({"all":"all  events"})


@api.route("/events/<event_id>", methods=["GET"])
def retrieve_single_event(event_id):
    return jsonify({"single": "Single event retrieved"})


@api.route("/events/<event_id>", methods=["PATCH"])
def update_event_info(event_id):
    return jsonify({"update": "Updated Event"})


@api.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    return jsonify({"delted": "deleted event"})

