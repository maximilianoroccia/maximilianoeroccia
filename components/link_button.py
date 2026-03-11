import reflex as rx 
from styles import Sizes, Spacings, styles, NumSize


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
                alt=title,
                width=Sizes.MEDIUM.value,
                height=Sizes.MEDIUM.value,
                border_radius=Sizes.XSMALL.value,
                border="1px solid #e6e6e8"
            ),
            rx.vstack(
                rx.text(title),
                rx.text(body),
                color= styles.TextColor.LIGHT.value,
                spacing=Spacings.ZERO.value,
                align="start"
            ),
            align="center",
            width=styles.TOTAL_WIDTH
        ),
        on_click=rx.redirect(path=url, is_external=is_external),
        width=styles.TOTAL_WIDTH,
        height="auto",
        padding_y=Sizes.XSMALL.value,
        padding_x=Sizes.SMALL.value,
        variant="classic"
    )