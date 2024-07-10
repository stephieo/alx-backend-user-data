#!/usr/bin/env python3
""" managing API authentication"""
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """class to manage API authentication"""

    def __init__(self):
        """initialization"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """doccccdocccc"""
        return False

    def authorization_header(self, request=None) -> str:
        """docccdoccc"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """socccdoccc"""
        return None

