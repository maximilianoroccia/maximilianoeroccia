import reflex as rx
import utils as utils
from components import navbar
from views import header, links
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
               links(),
                width=styles.MAX_WIDTH,
                max_width=styles.BIG_WIDTH,
                margin_y=styles.Spacings.SMALL.value,
                padding=styles.Sizes.SMALL.value
           ) 
        )
    )