#!/usr/bin/env python3
""" Basic Authentication"""
from flask import Flask, request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class"""
    pass
