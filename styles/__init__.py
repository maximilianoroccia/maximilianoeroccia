"""Paquete de estilos"""

from .styles import Sizes, Spacings, NumSize, BASE_STYLE, STYLESHEETS
from .colors import PageColor, TextColor
from .fonts import Font, FontWeight


__all__ = [
    "Sizes", "Spacings", "BASE_STYLE", "STYLESHEETS",
    "PageColor", "TextColor",
    "Font", "FontWeight",
    "NumSize"
]