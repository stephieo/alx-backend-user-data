#!/usr/bin/env python3
""" Basic Authentication"""
from flask import Flask, request
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic Auth class"""
    def __init__(self):
        """initialization"""
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns Base64 part of Authorization header"""
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif authorization_header[:6] != "Basic ":
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        elif type(base64_authorization_header) is not str:
            return None

        try:
            bytestring = base64.b64decode(base64_authorization_header)
        except Exception:
            return None

        return bytestring.decode('utf-8')
