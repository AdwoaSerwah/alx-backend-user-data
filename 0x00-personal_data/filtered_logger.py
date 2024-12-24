#!/usr/bin/env python3
"""
Module to filter and obfuscate Personally Identifiable Information (PII)
in log messages.
"""

import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Filters out specified fields in a log message and replaces them with
    the redaction string.

    Args:
        fields (list): List of fields to obfuscate.
        redaction (str): String used to obfuscate the fields.
        message (str): Log message containing the data to be obfuscated.
        separator (str): Character used to separate fields in the message.

    Returns:
        str: The obfuscated log message.
    """
    return re.sub(
        r'({}=[^{}]+)'.format('|'.join(fields), separator),
        lambda x: f"{x.group(0).split('=')[0]}={redaction}",
        message
    )
