#!/usr/bin/python3
"""Djist: Messages
"""
__author__ = "llelse"
__version__ = "0.1.0"
__license__ = "GPLv3"


# pylint: disable=line-too-long


# General messages
GENERAL_ERROR = "Could not complete because %s"
EVAL_ATTEMPT = "Tried to evaluate expression (%s)"
EVAL_ERROR = "Could not evaluate because %s"
DATE_FORMAT_ERROR = "The %s date format string (%s) is invalid"
INDEX_OUT_OF_RANGE = "Invalid index (%s) for list/array length (%s)"
INVALID_DICT_KEY = "Invalid key (%s) for dictionary/object"
INVALID_LIST_INDEX = "Invalid index (%s) for list/array"
JSON_DECODE_ERROR = "The JSON data file contains an error: %s"
KEY_VALUE = "Key (%s) has value (%s)"
UNEXPECTED_TYPE = "Unexpected data type (%s)"

# Help
HELP_LOG_LEVEL = "level of information to output to log file, or quiet for no logging"
HELP_CONSOLE_LEVEL = (
    "level of information sent to console, or quiet for no messages (default:)"
)
HELP_SCAN = "scan a template to determine data fields"
HELP_SCAN_TEMPLATE = "individual template to scan"
HELP_SCAN_DATASET = (
    "check if dataset contains the required fields to process the template"
)
HELP_RUN = "process an individual template"
HELP_RUN_TEMPLATE = "individual template to process. a dataset should also be specified when using this option."
HELP_RUN_DATASET = "dataset to use for individual template"
HELP_RUN_OUTPUT = "location to save the processed template"
HELP_JOB = "run a job using a config file"
HELP_JOB_CONFIG = "job configuration file (default: 'config.json')"


# Filter messages
FILTER_GENERAL = "Could not be applied: %s"
FILTER_DEFAULT_TYPE_WARNING = "%s filter: Expected type (%s) but found (%s)"
FILTER_DEFAULT_VALUE_INFO = "%s filter: Default value (%s) was used (argument %s)"
FILTER_VALUE_TYPE_WARNING = "%s filter: Unexpected value type (%s)"

FILTER_DICTSORT_ERROR = (
    "dictsort filter: Could not be applied. Key (%s) was not found in all list items"
)
FILTER_DICTSORTREVERSED_ERROR = "dictsortreversed filter: Could not be applied. Key (%s) was not found in all list items"
FILTER_DIVISIBLEBY_ERROR = (
    "divisibleby filter: Value (%s) or argument (%s) has an unexpected zero value"
)
FILTER_GET_DIGIT_ARG_ERROR = (
    "get_digit filter: Expected digit in range 1-%s. Invalid digit (%s) given"
)

# Processor
PROC_GETDATA_ERROR_NONKEY = "Key (%s) is not in dataset, and isn't a number"
PROC_GETDATA_INVALID_RETURN = "Invalid return type (%s)"
PROC_GETDATA_LIST_1 = "Invalid index (%s)"
