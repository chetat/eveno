from flask import jsonify

# Error handler


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


class BadRequest(Exception):
    status_code = 400

    def __init__(self, message, success=False, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.success = success

        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['success'] = self.success
        rv['message'] = self.message
        return rv


class ExistingResource(BadRequest):
    status_code = 409


class UnAuthorized(BadRequest):
    status_code = 401


class NotFound(BadRequest):
    status_code = 404


class InternalServerError(BadRequest):
    status_code = 500


class MethodNotAllowed(BadRequest):
    status_code = 405


class Forbiden(BadRequest):
    status_code = 403
