#!/usr/bin/env python3
""" Basic Authentication"""
from flask import Flask, request
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns user email and password from  the b64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) is not str:
            return None, None
        elif ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':')
        return (credentials[0], credentials[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        returns user based on email and password
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        matched_users = User().search({'email': user_email})
        if matched_users == []:
            return None

        for user in matched_users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth abd retrieves user instance
        """
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            base64_auth_header = self.extract_base64_authorization_header(auth_header)
            if base64_auth_header is not  None:
                decoded_base64_header = self.decode_base64_authorization_header(base64_auth_header)
                if decoded_base64_auth_header is not None:
                    user_creds = self.extract_user_credentials(decoded_base64_header)
                    if user_creds is not None:
                    user = self.user_object_from_credentials(user_creds)
                    if user is not None:
                        return user
        return None
