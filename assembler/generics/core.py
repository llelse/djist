#!/usr/bin/python3


"""
Site Assembler: Generic functions
"""

__author__ = "llelse"
__version__ = "0.1.0"
__license__ = "GPLv3"


def evaluate(exp, vars):
    pass
    # parser = expression.Expression_Parser(variables=vars)
    # return parser.parse(exp)


def sign(number: int or float) -> int:
    """Returns 1 for values '> 0', and 0 for values ' <= 0'"""
    return 1 - (number <= 0)


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
        '"': '&#34;',
        "'": '&#39;',
        # '--': '<br />'
    }


def esc_html():
    return {
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;',
        '"': '&quot;',
        "'": '&#x27;',
    }


def esc_js():
    return {
        '<': '\\u003C',
        '>': '\\u003E',
        '"': '\\u0022',
        "'": '\\u0027',
        '\r': '\\u000D',
        '\n': '\\u000A',
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


def type_match(match_object: object, match: str or tuple) -> bool:
    """Match type by string"""
    if isinstance(match, str):
        match = (match,)
    if 'any' in match:
        return True
    if 'number' in match:
        match = ('int', 'float') + match
    for match_type in match:
        if str(match_object) in f"<class '{match_type}'>":
            return True
    return False
