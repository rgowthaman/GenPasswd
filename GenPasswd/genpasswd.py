from . import functions
from . import getargument


def password():
    return getargument.password()


def passGen(given_tuple):
    length, ignore, only, include, repeat = given_tuple
    try:
        return functions.main(length, ignore, only, include, repeat)
    except ValueError:
        raise ValueError
