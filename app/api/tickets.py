from app.api import api
from flask import jsonify, request
from models import db, Tickets
from datetime import datetime
from Exceptions import NotFound, MethodNotAllowed, \
    Forbiden, InternalServerError, ExistingResource,\
    BadRequest, AuthError


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
def get_tickets():
    try:
        tickets = Tickets.query.all()
        return jsonify({
            "success": True,
            "data": [ticket.serialize for ticket in tickets]
        })
    except Exception as e:
        raise InternalServerError("Failed to fetch tickets")


@api.route('events/tickets', methods=["POST"])
def new_ticket():
    event_id = request.json.get("event_id", None)
    price = request.json.get("price", None)
    quantity = request.json.get("quantity", None)

    if not event_id or not quantity or not price:
        raise BadRequest("Provide valid request body")

    try:
        new_ticket = Tickets(event_id=event_id,
                             available=quantity,
                             price=price)
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
def get_ticket(ticket_id):
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


@api.route('events/tickets/<ticket_id>', methods=["PATCH"])
def update_tickets(ticket_id):
    event_id = request.json.get("event_id", None)
    price = request.json.get("price", None)
    quantity = request.json.get("quantity", None)

    try:
        ticket = Tickets.query.filter_by(id=ticket_id).first()
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError("Failed to fetch ticket")
    if not ticket:
        raise NotFound(f"Ticket with id {ticket_id} not found")
    try:
        if price:
            ticket.price = price
        if quantity:
            ticket.available = ticket.available + quantity
        ticket.updated_at = datetime.utcnow()
        Tickets.update(ticket)
    except Exception as e:
        print(e)
        db.session.rollback()
        raise InternalServerError("Problem updating tickets")

    return jsonify({
        "success": True,
        "data": ticket.serialize
    })
