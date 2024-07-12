#!/usr/bin/env python3
"""Session Auth class """
from flask import Flask, request
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authentication mechanism"""
    user_id_by_session_id = {}  # in-memory session storage

    def __init__(self):
        """initialization"""
        pass

    def create_session(self, user_id: str = None) -> str:
        """creates a session id for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = uuid.uuid4()
        user_id_by_session_id[session_id] = user_id

        return session_id
