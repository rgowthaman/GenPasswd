"""Generate a strong password which includes alphabets, numbers, special characters"""

__version__ = '1.1.3'

from .genpasswd import Password
from .functions import NoMultipleChoice, wanted_characters, include_characters, unwanted_characters, main
from .passgen import get_argument, gen_Pass, main
