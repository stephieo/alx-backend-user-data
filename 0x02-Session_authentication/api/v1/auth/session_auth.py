#!/usr/bin/env python3
"""Session Auth class """
from flask import Flask, request
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication mechanism"""
    pass
