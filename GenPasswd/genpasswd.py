from . import functions


class Password:
    def __init__(self, length=False, ignore=False, only=False, include=False, repeat=False):
        self.length = length
        self.ignore = ignore
        self.only = only
        self.include = include
        self.repeat = repeat

    def genPass(self):
        return functions.main(Length=self.length, Unwanted=self.ignore, Only_char=self.only, Include=self.include, Repeat=self.repeat)
