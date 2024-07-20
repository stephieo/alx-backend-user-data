#!/usr/bin/env python3
from user import User
import bcrypt
from db import DB
""" authentication module"""


def _hash_password(password: str) -> bytes:
    """ creates a salted hash of a password string"""
    pw_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pw_bytes, salt)
    return hashed_pass
