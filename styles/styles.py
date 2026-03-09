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
    SMALL = "2"
    MEDIUM = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "8"
    VERY_BIG = "9"
    
class ImageSize(Enum):
    SMALL = "10PX"
    MEDIUM = "20PX"
    DEFAULT = "30PX"
    LARGE = "50PX"

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
    "background": "url('/back.png') ", 
    "background_color": PageColor.DARK.value, 
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "width": MAX_WIDTH
    
}



