from enum import Enum


# Color表 https://i.stack.imgur.com/KTSQa.png
class Color(Enum):
    DEFAULT = ''
    RED = '\033[38;5;124m'
    GREEN = '\033[38;5;40m'
    BLUE = '\033[38;5;33m'
    PINK = '\033[38;5;206m'