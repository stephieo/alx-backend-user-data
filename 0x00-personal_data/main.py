#usr/bin/env python3
""" main file """
import logging 
import re
RedactingFormatter = __import__('filtered_logger').RedactingFormatter
get_db = __import__('filtered_logger').get_db

