#!/usr/bin/env python3
""" index  views for  blueprint"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route("/api/v1/status", methods=["GET"])
def status() -> str:
    """returns status of  API"""
    return jsonify({"status": "OK"})


@app_views.route("/unauthorized", methods=["GET"])
def error_401() -> str:
    """raises a 401 error"""
    abort(401, "Unauthorized")

@app_views.route("/forbidden", method=["GET"])
def error_403() -> str:
    """raises 403 error"""
    abort(403,"Forbidden")
