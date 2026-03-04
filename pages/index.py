import reflex as rx
import utils as utils
from components.navbar import navbar
from views.header import header

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
        header()
    )