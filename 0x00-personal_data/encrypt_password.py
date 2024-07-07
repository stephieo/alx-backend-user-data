#!/usr/bin/env python3
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """Hashes password using bcrypt
    """
    byt_psd = password.encode()
    salted = bcrypt.hashpw(byt_psd, bcrypt.gensalt())
    return salted


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check password validity"""
    return bcrypt.checkpw(str.encode(password), hashed_password)
