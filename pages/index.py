import reflex as rx
import utils as utils
from components import navbar
from views import header, links, proy_index
from styles import styles


class State(rx.State):
    pass

@rx.page(
    route="/",
    title= utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
           rx.vstack(
               header(),
               rx.separator(size=styles.NumSize.DEFAULT.value, color_scheme='blue'),
               links(),
               rx.separator(size=styles.NumSize.DEFAULT.value, color_scheme='blue'),
               proy_index(),
               rx.separator(size=styles.NumSize.DEFAULT.value, color_scheme='blue'),
               
               width=styles.TOTAL_WIDTH,
               max_width=styles.MAX_WIDTH,
               align="start",
               spacing="2",
               margin_y=styles.NumSize.SMALL.value,
               padding=styles.NumSize.SMALL.value
           )
        )
    )