import reflex as rx
import utils as utils

class State(rx.State):
    pass

@rx.page(
    route="/blog",
    title= utils.blog_title,
    description=utils.blog_description,
    image=utils.preview,
    meta=utils.blog_meta
)

def blog() -> rx.Component:
    return rx.box()