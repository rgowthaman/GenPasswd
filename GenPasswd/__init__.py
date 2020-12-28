"""Generate a strong password which includes alphabets, numbers, special characters"""

__version__ = '0.1.0'

from .genpasswd import password, pass_gen
from .getargument import password
from .functions import NoMultipleChoice, wanted_characters, include_characters, unwanted_characters, main
