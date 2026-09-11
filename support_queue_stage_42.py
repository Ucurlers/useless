# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SupportQueue
import os
import re

ANSI_COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "grey": "\033[90m",
}

color_codes = {}
for name, code in ANSI_COLORS.items():
    color_codes[name] = code
color_codes["black"] = "\033[30m"

def set_color(color, text=""):
    if color == "reset":
        return text
    return f"{color_codes.get(color, '')}{text}{ANSI_COLORS['reset']}"

def colored_print(color, *args, **kwargs):
    print(set_color(color, *args), **kwargs)

def colored_input(color, prompt=""):
    if color == "reset":
        return input(prompt)
    print(set_color(color, prompt), end="")
    return input()

def get_color():
    return os.environ.get("SUPPORT_QUEUE_COLOR", "1")

def disable_colors():
    os.environ["SUPPORT_QUEUE_COLOR"] = "0"
