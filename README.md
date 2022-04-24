# GenPasswd

[![PyPI](https://img.shields.io/pypi/v/genpasswd)](https://pypi.python.org/pypi/genpasswd)
[![PyPI - License](https://img.shields.io/pypi/l/genpasswd)](https://github.com/rgowthaman/GenPasswd/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/genpasswd?color=red)](https://pypi.python.org/pypi/genpasswd)

To generate random and strong passwords.

## Installation

`pip install -U genpasswd`

## Usage

```
usage: genpasswd [options]

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show version number and exit.

to customize Password:
  -l , --length      to set length to the password
  -n , --ignore      to ignore unwanted characters to the password
  -i , --include     to include characters to the password
  -o , --only        to create password only using wanted characters
  -s , --separator   the separator character
  -c , --seplen      the length of characters between separator
  --repeat           to repeat the characters in the password (default : False)
  --separation       to separate password characters using separator (default : False)
```

###
To generate a random password and print it on the screen.
```
> genpasswd
kj(ot--4mJ1aeJ
```
###

To set the password length, Default password length is `8-16`.

```
> genpasswd -l 10
Q3m/vro|uR
```
###

Whether the characters in passwords repeat or not,
Default value of `repeat` is `False`.
```
> genpasswd -r
96Ndl;1D>jQu4Z2
```
###

You can include, ignore or using only `'alphabets'`, `'numbers'`, `'uppercase'`, `'lowercase'`, `'symbols'` and some `random characters` in generating password.
###

To ignore `numbers` in passwords. 

```
> genpasswd -n numbers
uyMXP‘$!ZSCYqzj
```
###
To ignore characters `a,b,c,d,e`
```
> genpasswd -n abcde
~}t"R‘jF'ksG8~E
```
###
To create a password only using `special characters`.

```
> genpasswd -o symbols -l 15
?)".=-_^[_‘~{.)
```
###
To include `a,b,c,d,e` characters in a password.
```
> genpasswd -o numbers -i abcde -l 15
78713d1e3d926a3
```
###
To separate characters in a password using separator.
```
> genpasswd -o numbers -i abcde -l 15 --separation
7871-3d1e-3d92-6a3
```
###
To separate characters in a password using separator `_` with `5` characters between each separator.
```
> genpasswd -o numbers -i abcde -l 15 -s _ -c 5 
78713_d1e3d_926a3
```

## Issues:

If you encounter any problems, please file an [issue](https://github.com/rgowthaman/GenPasswd/issues) along with a detailed description.