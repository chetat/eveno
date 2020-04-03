import os
from app.api import api
from flask import jsonify, request, _request_ctx_stack
import json

from Exceptions import AuthError
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'dev-b-gpi9-h.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'eveno-api'
CLIENT_ID = os.environ["CLIENT_ID"]

# https://dev-b-gpi9-h.auth0.com/authorize?audience=eveno-api&response_type=token&client_id=jcH8UbYzF5WPvLEDoA8sJDhqqEgR36xn&redirect_uri=http://localhost:5000/token


def get_token_auth_header():
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError("missing_authorization_header", status_code=401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError("invalid_header! Authorization header\
                         must start with Bearer ", status_code=401)
    elif len(parts) == 1:
        raise AuthError("invalid_header! Token not found", 401)
    elif len(parts) > 2:
        raise AuthError("invalid_header! Authorization header\
                        must be Bearer token", 401)
    token = parts[1]
    return token


def check_permissions(permission, payload):
    if not payload["permissions"]:
        raise AuthError(401, "UnAuthorized")
    if permission in payload["permissions"]:
        return True


def verify_decode_jwt(token):
    token = get_token_auth_header()
    json_url = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
    jwks = json.loads(json_url.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError('invalid_header!\
             Authorization malformed.', status_code=401)
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://"+AUTH0_DOMAIN+"/"
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError("token_expired! token is expired", status_code=401)
        except jwt.JWTClaimsError:
            raise AuthError("invalid_claims!\
                                incorrect claims\
                                please check the \
                                    audience and issuer", status_code=401)
        except Exception:
            raise AuthError("invalid_header\
                                Unable to parse authentication\
                                token.", status_code=401)
    raise AuthError("invalid_header! \
                        Unable to find appropriate key", status_code=401)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
