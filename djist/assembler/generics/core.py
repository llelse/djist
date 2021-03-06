#!/usr/bin/python3
"""Djist: Generic functions
"""
__author__ = "llelse"
__version__ = "0.2.0"
__license__ = "GPLv3"


import sys
from ..job import log


def close(status: int = None):
    log.stop_logging()
    sys.exit(status)


def evaluate(exp, vars):
    pass
    # parser = expression.Expression_Parser(variables=vars)
    # return parser.parse(exp)


def sign(number: int or float) -> int:
    """Returns 1 for values '> 0', and 0 for values ' <= 0'"""
    return 1 - (number <= 0)


def int_negate(number: int) -> int:
    """Turn positive to negative integer"""
    return number - (number * 2)


def convert_to_int(str_: str or int) -> int:
    """Convert a string (str) into a number (int)
    An empty string converts to 0
    """
    if isinstance(str_, int):
        return str_
    elif isinstance(str_, float):
        return int(str_)
    elif isinstance(str_, str) and len(str_) > 0:
        if str_.isdigit():
            return int(str_)
        joined = "".join(char for char in str_ if char.isdigit() or char in "-")
        try:
            return int(joined)
        except ValueError:
            return 0
    return 0


def convert_to_float(str_: str or float or int) -> float:
    """Convert a string (str) into a number (float)
    An empty string converts to 0
    """
    if isinstance(str_, float):
        return str_
    elif isinstance(str_, int):
        return float(str_)
    elif isinstance(str_, str) and len(str_) > 0:
        joined = "".join(char for char in str_ if char.isdigit() or char in ("-", "."))
        try:
            return float(joined)
        except ValueError:
            return 0.0
    return 0.0


def is_empty(obj):
    return len(obj) == 0


def not_empty(obj):
    return not is_empty(obj)


def is_none_or_empty(obj):
    return obj is None or len(obj) == 0


def not_none_or_empty(obj):
    return not is_none_or_empty(obj)


def web_safe_subs():
    return {
        '"': "&#34;",
        "'": "&#39;",
        # '--': '<br />'
    }


def esc_html():
    return {
        "<": "&lt;",
        ">": "&gt;",
        "&": "&amp;",
        '"': "&quot;",
        "'": "&#x27;",
    }


def esc_js():
    return {
        "<": "\\\\u003C",
        ">": "\\\\u003E",
        '\\"': "\\\\u0022",
        '"': "\\\\u0022",
        "\\'": "\\\\u0027",
        "'": "\\\\u0027",
        "\\r": "\\\\u000D",
        "\r": "\\\\u000D",
        "\\n": "\\\\u000A",
        "\n": "\\\\u000A",
    }


def substitute(subs: dict, text: str, reverse: bool = False) -> str:
    for k, v in subs.items():
        if reverse:
            text = text.replace(v, k)
        else:
            text = text.replace(k, v)
    return text


def web_safe_string(dirty_string: str):
    safe_string = substitute(web_safe_subs(), dirty_string)
    return safe_string


def web_safe_list(dirty_list: list):
    safe_list = []
    for x in dirty_list:
        safe_list.append(web_safe_string(x))
    return safe_list


def type_string(match_object: object) -> str:
    """Name of type, condensed"""
    if isinstance(match_object, type):
        replace = str(match_object)
    else:
        replace = str(type(match_object))
    return replace.replace("<class '", "").replace("'>", "")


def types(match: object or tuple) -> str:
    """String of type(s)"""
    return_types = ""
    if isinstance(match, tuple):
        separator = ""
        for match_object in match:
            return_types += separator + type_string(match_object)
            separator = ", "
    else:
        return_types += type_string(match)
    return return_types


def type_match(match_object: object, match: str or tuple) -> bool:
    """Match type by string"""
    if isinstance(match, str):
        match = (match,)
    if "any" in match:
        return True
    if "number" in match:
        match = ("int", "float") + match
    for match_type in match:
        if type_string(match_object) == match_type:
            return True
    return False


def index_in_list(index: int, check_list: list) -> bool:
    length = len(check_list)
    return -length <= index < length
