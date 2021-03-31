from . import functions


class Password:
    def __init__(self, length=False, ignore=False, only=False, include=False, repeat=False, separator=False, separator_length=False, separation=False):
        self.length = length
        self.ignore = ignore
        self.only = only
        self.include = include
        self.repeat = repeat
        self.separator_length = separator_length
        self.separator = separator if separator else separation

    def generate(self):
        return functions.main(Length=self.length, Unwanted=self.ignore, Only_char=self.only, Include=self.include, Repeat=self.repeat, Seperator_length=self.separator_length, Seperator=self.separator)
