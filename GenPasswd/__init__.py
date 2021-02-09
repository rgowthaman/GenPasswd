"""Generate a strong password which includes alphabets, numbers, special characters"""

__version__ = '1.1.6'

from .genpasswd import Password
from .functions import NoMultipleChoice, wanted_characters, include_characters, unwanted_characters, main
from .__main__ import get_argument, gen_Password, main
