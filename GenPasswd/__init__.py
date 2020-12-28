"""Generate a strong password which includes alphabets, numbers, special characters"""

__version__ = '1.0.0'

from .genpasswd import password, passGen
from .getargument import password
from .functions import NoMultipleChoice, wanted_characters, include_characters, unwanted_characters, main
