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
@requires_auth("create:events")
def new_event(token):
    return jsonify({"events": "new events"})


@api.route("/events", methods=["GET"])
@requires_auth("read:events")
def retrieve_all_events(token):
    try:
        users = Events.query.all()
    except Exception as e:
        print(e)
        raise InternalServerError(
            "Internal Server Error! Could not retrieve users.")

    return jsonify({"success": True,
                    "data": [user.serialize for user in users]
                    })


@api.route("/events/<event_id>", methods=["GET"])
@requires_auth("read:events")
def retrieve_single_event(token, event_id):
    return jsonify({"single": "Single event retrieved"})


@api.route("/events/<event_id>", methods=["PATCH"])
@requires_auth("update:events")
def update_event_info(token, event_id):
    return jsonify({"update": "Updated Event"})


@api.route("/events/<event_id>", methods=["DELETE"])
@requires_auth("delete:events")
def delete_event(token, event_id):
    return jsonify({"delted": "deleted event"})
