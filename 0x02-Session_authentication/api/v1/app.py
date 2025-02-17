#!/usr/bin/env python3
""" Routes of flask app"""
import os
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
AUTH_TYPE = os.getenv("AUTH_TYPE")

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def before_request_handler():
    """executes before all requests"""
    cookie = auth.session_cookie(request)
    if auth is None:
        pass
    elif request.path not in ['/api/v1/status/',
                              '/api/v1/status',
                              '/api/v1/unauthorized/',
                              '/api/v1/unauthorized',
                              '/api/v1/forbidden/',
                              '/api/v1/auth_session/login/',
                              '/api/v1/auth_session/login',
                              '/api/v1/forbidden']:
        if auth.authorization_header(request) is None and cookie is None:
            abort(401)
        request.current_user = auth.current_user(request)
        if auth.current_user(request) is None:
            abort(403)


@app.errorhandler(401)
def unauth_request(error) -> str:
    """handles 401 error"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_request(error) -> str:
    """ handles 403  error"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = os.getenv("API_PORT", "5000")
    app.run(debug=True, host=API_HOST, port=API_PORT)
