#!/usr/bin/env python3
""" filter personal data"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        res = filter_datum(self.fields, self.REDACTION,
                           super(RedactingFormatter, self).format(record),
                           self.SEPARATOR)
        return res


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns a log message obfuscated
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
                  is separating all fields in the log line (message)
    """
    for field in fields:
        obs_msg = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return obs_msg
