import reflex as rx 
from styles import Sizes, Spacings, styles, ImageSize


def link_button(
    title: str,
    body: str,
    image: str,
    url: str | None=None,
    is_external= True
) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=ImageSize.DEFAULT.value,
                height=ImageSize.DEFAULT.value,
                border_radius= "5px",
                border="1px solid #b6b6b8",
                alt=title
            ),
            rx.vstack(
                rx.text(title),
                rx.text(body),
                spacing=Spacings.ZERO.value
            ),
            align="center",
            width=styles.MAX_WIDTH,
        ),
        on_click=rx.redirect(path=url, is_external=is_external),
        width=styles.MAX_WIDTH,
        padding=Sizes.SMALL.value
    )