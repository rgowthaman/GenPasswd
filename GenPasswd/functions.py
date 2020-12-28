import random


class NoMultipleChoice(Exception):
    pass


def wanted_characters(characters):
    possibility = ''
    try:
        character = [character for character in characters.split(',')]
    except Exception:
        raise NoMultipleChoice
    for choice in character:
        if choice.lower() == 'alphabets':
            possibility += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if choice.lower() == 'lowercase':
            possibility += 'abcdefghijklmnopqrstuvwxyz'
        if choice.lower() == 'uppercase':
            possibility += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if choice.lower() == 'numbers':
            possibility += '0123456789'
        if choice.lower() == 'symbols':
            possibility += str('''!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\''')
        if not choice.lower() in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
            for unwanteds in choice:
                possibility += unwanteds
    return possibility


def include_characters(adding, characters):
    possibility = characters
    try:
        character = [character for character in adding.split(',')]
    except Exception:
        raise NoMultipleChoice
    for choice in character:
        if choice.lower() == 'alphabets':
            for alphabet in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if alphabet not in possibility:
                    possibility += alphabet
        if choice.lower() == 'lowercase':
            for alphabet in "abcdefghijklmnopqrstuvwxyz":
                if alphabet not in possibility:
                    possibility += alphabet
        if choice.lower() == 'uppercase':
            for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if alphabet not in possibility:
                    possibility += alphabet
        if choice.lower() == 'numbers':
            for number in "0123456789":
                if number not in possibility:
                    possibility += number
        if choice.lower() == 'symbols':
            for symbol in str('''!"%&'()*+,-./:;<=>?@[]^_`{|}~”$‘~#\\'''):
                if symbol not in possibility:
                    possibility += symbol
        if not choice.lower() in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
            for unwanteds in choice:
                if unwanteds not in possibility:
                    possibility += unwanteds
    return possibility


def unwanted_characters(unwanted, possibility):
    unwanted_lists, unwanted_characters_lists = '', ''
    try:
        choices = [characters for characters in unwanted.split(',')]
    except Exception:
        raise NoMultipleChoice
    if unwanted == ',' or ',,,' in unwanted or ',,' in unwanted:
        possibility = possibility.replace(',', '')
    for choice in choices:
        if choice == 'alphabets':
            for alphabet in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                possibility = possibility.replace(alphabet, '')
        if choice == 'uppercase':
            for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                possibility = possibility.replace(alphabet, '')
        if choice == 'lowercase':
            for alphabet in "abcdefghijklmnopqrstuvwxyz":
                possibility = possibility.replace(alphabet, '')
        if choice == 'numbers':
            for number in "0123456789":
                possibility = possibility.replace(number, '')
        if choice == 'symbols':
            for symbol in str('''!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\'''):
                possibility = possibility.replace(symbol, '')
        if not choice in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
            for unwanteds in choice:
                possibility = possibility.replace(unwanteds, '')
    return possibility


def main(length=False, unwanted=False, only_char=False, include=False, repeat='y'):
    possibility = str(
        '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\''')
    if unwanted:
        if only_char:
            possibility = wanted_characters(only_char)
        if include:
            possibility = include_characters(include, possibility)
        possibility = unwanted_characters(unwanted.lower(), possibility)
    else:
        if only_char:
            possibility = wanted_characters(only_char)
        if include:
            possibility = include_characters(include, possibility)
    if repeat is None or repeat.lower() == 'y':
        repeat = 'y'
    if not length and not only_char:
        length = random.randint(8, 16)
    elif not length and only_char:
        return ValueError('[-] Password length must be given.')
    possibility = (possibility * int(length)) if repeat.lower() == 'y' else possibility
    if length and ((int(length) > len(possibility)) or int(length) > 72):
        return ValueError('[-] Password length must be less.')
    return "Password : " + "".join(random.sample(possibility, int(length)))
