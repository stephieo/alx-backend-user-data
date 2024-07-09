#!/usr/bin/env python3
""" Routes of flask app"""
import os
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(401)
def unauth_request(error) -> str:
    """handles 401 error"""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = os.getenv("API_PORT", "5000")
    app.run(debug=True, host=API_HOST, port=API_PORT)
