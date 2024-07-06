#!/usr/bin/python3
""" filter personal data"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """ returns a log message obfuscated"""
    for field in fields:
        obs_msg = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return obs_msg
