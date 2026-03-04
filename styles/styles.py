import reflex as rx
from enum import Enum
from .colors import PageColor, TextColor
from .fonts import Font, FontWeight

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Truculenta:opsz,wght@12..72,100..900&display=swap"
]

# CONSTANTES
MAX_WIDTH = "100%"
BIG_WIDTH = "600px"

# SIZES

class Sizes(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

class Spacings(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL = "2"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# STYLES

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.REGULAR.value,
    "background_color": PageColor.DARK.value,  
    "background_image": "back.png",
    
}

