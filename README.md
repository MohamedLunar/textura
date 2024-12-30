# Textura

`Textura` is a lightweight Python library that allows you to easily add stylish and colorful text to your terminal using ANSI escape sequences. It includes predefined colors, background colors, and text styles such as bold, underline, and reversed text.

## Features:
- **Foreground Colors**: Red, Green, Blue, Yellow, Magenta, Cyan, White
- **Background Colors**: Red, Green, Blue, Yellow, Magenta, Cyan, White
- **Text Styles**: Bold, Underlined, Reversed
- **Helper Functions**: For easy text styling

## Installation

You can easily install `Textura` via pip:

```bash
pip install textura
```
# Usage
Here is full usage of package:
```python
import textura
from textura import Fore, Back, Style, bold, underline, reversed, bold_bg

# 1. Basic Foreground Colors
print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Fore.BLUE + "This is blue text")

# 2. Basic Background Colors
print(Back.YELLOW + "This is text with a yellow background")
print(Back.CYAN + "This is text with a cyan background")

# 3. Combine Foreground and Background Colors
print(Fore.RED + Back.YELLOW + "Red text with a yellow background")
print(Fore.CYAN + Back.MAGENTA + "Cyan text with a magenta background")

# 4. Text Styles
print(Style.BOLD + "This is bold text")
print(Style.UNDERLINE + "This is underlined text")
print(Style.REVERSED + "This is reversed text")

# 5. Using Helper Functions for Styling
print(bold("This is bold text"))
print(underline("This is underlined text"))
print(reversed("This is reversed text"))

# 6. Bold text with custom foreground and background color
print(bold_bg("Bold text with red foreground and yellow background", Fore.RED, Back.YELLOW))

# 7. Advanced Styling
print(Style.BOLD + Style.UNDERLINE + Fore.MAGENTA + Back.CYAN + "Bold and Underlined Magenta Text on Cyan Background")
print(Style.REVERSED + Fore.GREEN + Back.RED + "Reversed Green Text on Red Background")

# 8. Combine Helper Functions for Dynamic Styling
print(bold(underline("Bold and Underlined Text")))
print(bold_bg(underline("Bold, Underlined, and Colored Text"), Fore.WHITE, Back.BLUE))

# 9. Fully Styled and Dynamic Outputs
print(bold(Fore.YELLOW + Back.BLACK + "Bold Yellow Text on Black Background"))
print(underline(Fore.CYAN + "Underlined Cyan Text"))
# 10. Reset the text to default
print(Fore.RED + "Red text" + style.RESET + "reseted to default")
```
