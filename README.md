# GenPasswd

[![PyPI](https://img.shields.io/pypi/v/genpasswd.svg)](https://pypi.python.org/pypi/genpasswd)
[![PyPI - License](https://img.shields.io/pypi/l/genpasswd)](https://github.com/Gowthaman1401/GenPasswd/blob/main/LICENSE)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Gowthaman1401/GenPasswd?color=orange&include_prereleases)](https://github.com/Gowthaman1401/GenPasswd/releases)

To generate random and strong passwords.

## Installation

`pip install genpasswd`

## Usage

To generate a random password and print it on the screen.
```python
from genpasswd import *
arg = Password()
passwd = arg.genPass()
print(passwd)
```

## Some Other Examples

To set the password length, Default password length is `8-16`.
```python
from genpasswd import *
arg = Password(length=5)
passwd = arg.genPass()
print(passwd)
```
Whether the characters in passwords repeat or not,
Default value of `repeat` is `True`.
```python
from genpasswd import *
arg = Password(repeat=False)  
passwd = arg.genPass()
print(passwd)
```
To ignore Characters, Numbers or special Characters in passwords. 

```python
from genpasswd import *
# to ignore or avoid alphabets
arg = Password(ignore='alphabets')
passwd = arg.genPass()
print(passwd)
```
To include Characters, Numbers or special Characters in passwords.

```python
from genpasswd import *
# to include numbers in a password
arg = Password(include='numbers')
passwd = arg.genPass()
print(passwd)
```
To create a password only using Characters, Numbers or special Characters.

```python
from genpasswd import *
# to generate a password only using characters 'abcde'
arg = Password(only='abcde', length=5)
passwd = arg.genPass()
print(passwd)
```
You can include, ignore or using only `'alphabets'`, `'numbers'`, `'uppercase'`, `'lowercase'`, `'symbols'` in generating password.
