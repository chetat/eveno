from app.api import api
from flask import jsonify, request
from models import db, Tickets
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource,\
    BadRequest, AuthError
from .authhelpers import requires_auth


@api.errorhandler(NotFound)
@api.errorhandler(Forbiden)
@api.errorhandler(MethodNotAllowed)
@api.errorhandler(InternalServerError)
@api.errorhandler(BadRequest)
@api.errorhandler(ExistingResource)
def api_error(error):
    payload = dict(error.payload or ())
    payload['code'] = error.status_code
    payload['message'] = error.message
    payload['success'] = error.success
    return jsonify(payload), error.status_code


@api.route('events/tickets')
@requires_auth("read:tickets")
def get_tickets(token):
    try:
        tickets = Tickets.query.all()
        return jsonify({
            "success": True,
            "data": [ticket.serialize for ticket in tickets]
        })
    except Exception as e:
        raise InternalServerError("Failed to fetch tickets")


@api.route('events/tickets', methods=["POST"])
@requires_auth("create:tickets")
def new_ticket(token):
    event_id = request.json.get("event_id", None)
    attender_email = request.json.get("email", None)

    if not event_id or not attender_email:
        raise BadRequest("Provide valid request body")

    try:
        new_ticket = Tickets(event_id=event_id, attender_email=attender_email)
        Tickets.insert(new_ticket)
        return jsonify({
            "success": True,
            "data": new_ticket.serialize
        })
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError("Could not create new event ticket")


@api.route('events/tickets/<ticket_id>')
@requires_auth("read:tickets")
def get_ticket(token, ticket_id):
    try:
        ticket = Tickets.query.filter_by(id=ticket_id).first()
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError("Failed to fetch ticket")
    if not ticket:
        raise NotFound(f"Ticket with id {ticket_id} not found")
    else:
        return jsonify(ticket.serialize)
