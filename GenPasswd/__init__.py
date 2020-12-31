"""Generate a strong password which includes alphabets, numbers, special characters"""

__version__ = '1.1.2'

from .genpasswd import Password
from .functions import NoMultipleChoice, wanted_characters, include_characters, unwanted_characters, main
