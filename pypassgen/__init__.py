"""Generate a strong password which includes alphabets, numbers, special characters"""


from .passgen import get_argument
from .functions import PasswordLengthGreaterThanCharacterLength, PasswordLengthGreaterThanLimit, NoPasswordLength, NoMultipleChoice
from .functions import wanted_characters, include_characters, unwanted_characters, pass_gen