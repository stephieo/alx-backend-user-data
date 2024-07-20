#!/usr/bin/env python3
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def home_page() -> str:
    """homepage of flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """find user and register if non-existent"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "user already registered"}), 400
    # if user:
    # else:


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
