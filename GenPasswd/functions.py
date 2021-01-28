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
            for unwanted in choice:
                possibility += unwanted
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
            for temp_var in choice:
                if temp_var not in possibility:
                    possibility += temp_var
    return possibility


def unwanted_characters(unwanted, possibility):
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
        if choice not in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
            for temp_var in choice:
                possibility = possibility.replace(temp_var, '')
    return possibility


def main(Length=False, Unwanted=False, Only_char=False, Include=False, Repeat=False):
    possibility = str(
        '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\''')
    if Unwanted:
        if Only_char:
            possibility = wanted_characters(Only_char)
        if Include:
            possibility = include_characters(Include, possibility)
        possibility = unwanted_characters(Unwanted.lower(), possibility)
    else:
        if Only_char:
            possibility = wanted_characters(Only_char)
        if Include:
            possibility = include_characters(Include, possibility)
    Repeat = 'y' if Repeat is None or Repeat is True else 'n'
    if not Length and not Only_char:
        Length = random.randint(8, 16)
    elif not Length and Only_char:
        return ValueError('[-] Password length must be given.')
    possibility = (possibility * int(Length)) if Repeat.lower() == 'y' else possibility
    if Length and ((int(Length) > len(possibility)) or int(Length) > 72):
        return ValueError('[-] Password length must be less.')
    return "".join(random.sample(possibility, int(Length)))
