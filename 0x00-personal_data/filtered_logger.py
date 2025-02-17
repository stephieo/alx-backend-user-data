#!/usr/bin/env python3
""" filter personal data"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ use filter_datum to filter incoming logs"""
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


def get_logger() -> logging.Logger:
    """  return a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    log_handler = logging.StreamHandler()
    formatter = RedactingFormatter(List(PII_FIELDS))
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns connector to database"""
    connection = mysql.connector.connect(
                        database=os.getenv('PERSONAL_DATA_DB_NAME'),
                        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
                        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
                        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', " ")
                        )
    return connection


def main() -> None:
    """ main function here"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    fields = cursor.column_names
    for row in cursor:
        message = "".join("{}={}; ".format(k, v) for k, v in zip(fields, row))
        logger.info(message.strip())
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
