import reflex as rx
from enum import Enum
from .colors import PageColor, TextColor
from .fonts import Font, FontWeight

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Truculenta:opsz,wght@12..72,100..900&display=swap"
]

# CONSTANTES
TOTAL_WIDTH = "100%"
BUTTON_WIDTH = "400px"
MAX_WIDTH = "600px"

# SIZES

class Sizes(Enum):
    ZERO = "0px !important"
    XSMALL = "5PX"
    SMALL = "20px"
    MEDIUM = "30px"
    DEFAULT = "40px"
    LARGE = "50px"
    BIG = "80px"
    VERY_BIG = "100px"
    
class NumSize(Enum):
    ZERO = "0"
    SMALL = "2"
    MEDIUM = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "8"

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
    "color": TextColor.DARK.value,
    "background": "url('/back.png') ", 
    "background_color": PageColor.DARK.value, 
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "width": TOTAL_WIDTH
}



