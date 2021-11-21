import re


def isNumber(token):
    return re.match(r'^(0|[+\-]?[1-9][0-9]*)$', token)


def isChar(token):
    return re.match(r'^(\'.\')$', token)


def isBool(token):
    return re.match(r'^(true|false)$', token)


def isString(token):
    return re.match(r'^(\"[^\"]*\")$', token)
