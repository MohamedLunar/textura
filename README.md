<img src="TexturaLogo.png" width="480" height="150">

# Textura
Textura is a lightweight Python library for adding colors and styles to your terminal text. 🎨

# Features
- 🌟 Easy-to-use syntax.
- 🎨 Support for foreground and background colors.
- 📝 Text styles like bold, underline, and reversed.
- 🧽 Reset functionality to clear formatting.

# Installation
## #1 Automatically
📩 You Can install package by executing:
```bash
pip install textura
```
or
```bash
python -m pip install textura
```
## #2 Manually
You can install the package from the [realeases](https://github.com/MohamedLunar/textura/releases) and download the `textura.zip` file and unpack it and execute the following command in terminal
```bash
cd /sdcard/textura
python setup.py install
```
or
```bash
pip install -e /sdcard/textura
```
### NOTE:
if you're using linux or windows change the `/sdcard` to `desktop`
## Quick Start
You can try the package for the first time by:
```python
import textura
from textura import Fore, Style

print(Fore.RED + "This is a red text!" + Style.RESET)
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
