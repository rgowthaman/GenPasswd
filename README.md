# GenPasswd

To generate random and strong passwords

## Installation

[![PyPI](https://img.shields.io/pypi/v/genpasswd.svg)](https://pypi.python.org/pypi/genpasswd)
[![Downloads](https://pepy.tech/badge/genpasswd/month)](https://pepy.tech/project/genpasswd)

## Using command-prompt

`pip install genpasswd`

## Usage

Import the library.

```python
from genpasswd import password, pass_gen
```
This will generate a random password and print it on the screen.

```python
arg = password()
passwd = pass_gen(arg)
print(passwd)
```

### Some other options in generating password.
Getting password length
```python
arg = password(length=5)
passwd = pass_gen(arg)
print(passwd)
```
Whether the characters in passwords repeat or not
```python
# default value of repeat is 'True'
arg = password(repeat=False)  
passwd = pass_gen(arg)
print(passwd)
```
Characters to ignore in passwords.
```python
# to ignore alphabets
# you can also give 'numbers', 'uppercase', 'lowercase', 'symbols' to ignore then respectively
arg = password(ignore='alphabets')
# also give random unwanted characters (eg., ignore='abc' will ignore the lowercase 'a','b','c')
passwd = pass_gen(arg)
print(passwd)
```
Characters to include in passwords
```python
# to include alphabets
# you can also give 'numbers', 'uppercase', 'lowercase', 'symbols' to include then respectively
arg = password(include='alphabets')
# also give random unwanted characters (eg., include='abc' will include the lowercase 'a','b','c')
passwd = pass_gen(arg)
print(passwd)
```
Only characters in passwords
```python
# to generate password only using alphabets
# you can also give 'numbers', 'uppercase', 'lowercase', 'symbols' 
# to generate password only using then respectively
# length value must be given
arg = password(only='alphabets', length=16)
# also give random unwanted characters (eg., only='abc' will create password only using the lowercase 'a','b','c')
passwd = pass_gen(arg)
print(passwd)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
