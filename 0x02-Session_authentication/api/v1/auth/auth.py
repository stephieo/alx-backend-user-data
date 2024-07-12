#!/usr/bin/env python3
""" managing API authentication"""
from flask import Flask, request
from typing import List, TypeVar
import os


class Auth():
    """class to manage API authentication"""

    def __init__(self):
        """initialization"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """doccccdocccc"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True

        path = path.rstrip("/")
        stripped = [i.rstrip("/") for i in excluded_paths]
        if path in stripped:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """docccdoccc"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """socccdoccc"""
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request"""
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
