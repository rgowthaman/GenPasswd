import random

from . import constants
from . import exceptions


class PasswordGenerator:
    def __init__(self, length=False, ignore=False, only=False, include=False, repeat=False, separator=False,
                 separator_length=False, separation=False):
        self.__password = None
        self.__available_char = None
        self.__possibility = None
        self.__error = None
        self.length = length
        self.ignore = ignore
        self.only = only
        self.include = include
        self.repeat = repeat
        self.separator_length = separator_length
        self.separator = separator if separator else separation

    def __all_possible_chars(self):
        self.__possibility = constants.POSSIBLE_UPPERCASE_CHARS + constants.POSSIBLE_LOWERCASE_CHARS + constants.POSSIBLE_NUMBERS + constants.POSSIBLE_SPECIAL_CHARS
        self.__available_char = {"alphabets": constants.POSSIBLE_UPPERCASE_CHARS + constants.POSSIBLE_LOWERCASE_CHARS,
                                 "uppercase": constants.POSSIBLE_UPPERCASE_CHARS,
                                 "lowercase": constants.POSSIBLE_LOWERCASE_CHARS,
                                 "numbers": constants.POSSIBLE_NUMBERS,
                                 "symbols": constants.POSSIBLE_SPECIAL_CHARS
                                 }

    def __set_length(self):
        if not self.length:
            if not self.only:
                self.length = random.randint(constants.DEFAULT_MIN_PASS_LEN, constants.DEFAULT_MAX_PASS_LEN)
            else:
                self.__error = ValueError('[-] Password length must be given.')

    def __add_only_wanted(self):
        possibility = constants.EMPTY_STRING
        try:
            choices = [character for character in self.only.split(',')]
            for choice in choices:
                if choice.lower() in self.__available_char:
                    possibility += self.__available_char[choice.lower()]
                if not choice.lower() in self.__available_char:
                    for char in choice:
                        possibility += char
        except Exception:
            raise exceptions.GenpasswdException
        self.__possibility = possibility

    def __remove_unwanted(self):
        try:
            choices = [characters for characters in self.ignore.split(',')]
            if self.ignore == ',' or ',,,' in self.ignore or ',,' in self.ignore or len(choices) > 0:
                possibility = self.__possibility.replace(',', constants.EMPTY_STRING)
                for choice in choices:
                    if choice.lower() in self.__available_char:
                        for char in self.__available_char[choice.lower()]:
                            possibility = possibility.replace(char, constants.EMPTY_STRING)
                    if choice not in self.__available_char:
                        for char in choice:
                            possibility = possibility.replace(char, constants.EMPTY_STRING)
                self.__possibility = possibility
        except Exception:
            raise exceptions.GenpasswdException

    def __include_characters(self):
        possibility = self.__possibility
        try:
            choices = [character for character in self.include.split(',')]
            for choice in choices:
                if choice.lower() in self.__available_char:
                    for char in self.__available_char[choice.lower()]:
                        if char not in possibility:
                            possibility += char
                if not choice.lower() in self.__available_char:
                    for char in choice:
                        if char not in possibility:
                            possibility += char
        except Exception:
            raise exceptions.GenpasswdException
        self.__possibility = possibility

    def __repeat_char(self):
        if self.repeat is None or self.repeat is True:
            self.__possibility *= self.length

    def __check(self):
        if self.length and ((self.length > len(
                self.__possibility)) or self.length > constants.PASSWORD_LENGTH_LIMIT) and self.__error is None:
            self.__error = ValueError('[-] Password length must be less.')

    def __separated_pass(self):
        if type(self.separator) is bool:
            self.separator = constants.DEFAULT_SEPARATOR
        if not self.separator_length:
            self.separator_length = constants.DEFAULT_SEPARATE_LENGTH
        final_password = constants.EMPTY_STRING
        for i in range(len(self.__password)):
            final_password += self.separator + self.__password[i] if i % self.separator_length == 0 and i != 0 else \
                self.__password[i]
        return final_password

    def __filter(self):
        if self.only:
            self.__add_only_wanted()
        if self.include:
            self.__include_characters()
        if self.ignore:
            self.__remove_unwanted()
        self.__repeat_char()

    def generate(self):
        self.__all_possible_chars()
        self.__set_length()
        self.__filter()
        self.__check()
        if self.__error is not None:
            return self.__error
        self.__password = constants.EMPTY_STRING.join(random.sample(self.__possibility, self.length))
        return self.__separated_pass() if self.separator or self.separator_length else self.__password
