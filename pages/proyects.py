import reflex as rx
import utils as utils

class State(rx.State):
    pass

@rx.page(
    route="/proyects",
    title= utils.proyects_title,
    description=utils.proyects_description,
    image=utils.preview,
    meta=utils.proyects_meta
)

def proyects() -> rx.Component:
    return rx.box()