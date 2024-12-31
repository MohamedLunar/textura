# textura/textura.py

class ANSI:
    RESET = '\033[0m'
    RESET_ALL = '\033[0m'

    # Foreground Colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Background Colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'
    BG_YELLOW = '\033[43m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'


# Fore, Back, and Style classes for convenience
class Fore:
    RED = ANSI.RED
    GREEN = ANSI.GREEN
    BLUE = ANSI.BLUE
    YELLOW = ANSI.YELLOW
    MAGENTA = ANSI.MAGENTA
    CYAN = ANSI.CYAN
    WHITE = ANSI.WHITE


class Back:
    RED = ANSI.BG_RED
    GREEN = ANSI.BG_GREEN
    BLUE = ANSI.BG_BLUE
    YELLOW = ANSI.BG_YELLOW
    MAGENTA = ANSI.BG_MAGENTA
    CYAN = ANSI.BG_CYAN
    WHITE = ANSI.BG_WHITE


class Style:
    BOLD = ANSI.BOLD
    UNDERLINE = ANSI.UNDERLINE
    REVERSED = ANSI.REVERSED
    RESET = ANSI.RESET


# Helper Functions
def bold(text):
    """Return text in bold style"""
    return Style.BOLD + text + ANSI.RESET

def underline(text):
    """Return text with underline style"""
    return Style.UNDERLINE + text + ANSI.RESET

def reversed(text):
    """Return text with reversed colors"""
    return Style.REVERSED + text + ANSI.RESET

def bold_bg(text, fore_color, back_color):
    """Return text in bold with custom foreground and background color"""
    return fore_color + back_color + Style.BOLD + text + ANSI.RESET