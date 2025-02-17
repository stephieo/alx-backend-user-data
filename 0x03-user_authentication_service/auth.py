#!/usr/bin/env python3
from user import User
import bcrypt
from db import DB
import uuid
""" authentication module"""


def _hash_password(password: str) -> bytes:
    """ creates a salted hash of a password string"""
    pw_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pw_bytes, salt)
    return hashed_pass


def _generate_uuid() -> str:
    """return string of uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register users"""
        user = self._db.find_user_by(email=email)

        if user:
            raise ValueError(f'User {email} already exists')
        else:
            hash_pw = _hash_password(password)
            saved_user = self._db.add_user(email, hash_pw)
            return saved_user

    def valid_login(self, email: str, password: str) -> bool:
        """validate user password"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                pass_byte = password.encode('utf-8')
                passwd_ck = bcrypt.checkpw(pass_byte, user.hashed_password)
                return (True if passwd_ck else False)
            return False
        except Exception:
            return False
