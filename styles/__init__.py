"""Paquete de estilos"""

from .styles import Sizes, Spacings, ImageSize, BASE_STYLE, STYLESHEETS
from .colors import PageColor, TextColor
from .fonts import Font, FontWeight


__all__ = [
    "Sizes", "Spacings", "BASE_STYLE", "STYLESHEETS",
    "PageColor", "TextColor",
    "Font", "FontWeight",
    "ImageSize"
]