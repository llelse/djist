#!/usr/bin/python3
"""Djist: Config
"""
__author__ = "llelse"
__version__ = "0.1.0"
__license__ = "GPLv3"


from io import TextIOWrapper


# Mode
MODE_SCAN: bool
MODE_RUN: bool
MODE_JOB: bool

# Logging
LOG_CONSOLE: bool
LOG_CONSOLE_LEVEL: str
LOG_FILE: bool
LOG_FILE_LEVEL: str
LOG_FILE_LOCATION: str

# File streams
IO_LOG: TextIOWrapper
IO_CONFIG: TextIOWrapper
IO_TEMPLATE: TextIOWrapper
IO_DATASET: TextIOWrapper
IO_OUTFILE: TextIOWrapper
