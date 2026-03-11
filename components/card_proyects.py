import reflex as rx 
from styles import styles

def card_proyects(
    title: str,
    url: str,
    image: str,
    description: str,
    is_external = False
) -> rx.Component:
    return rx.card(
        rx.link(
            rx.hstack(
                rx.avatar(
                    src=image,
                    size=styles.NumSize.BIG.value,
                    fallback="PD"
                ),
                rx.vstack(
                    rx.heading(title, color=styles.TextColor.DARK.value),
                    rx.text(description, color=styles.TextColor.DARK.value)
                ),
                background_color= styles.PageColor.EXTRA_LIGHT.value,
                padding=styles.Sizes.SMALL.value,
                align="center",
                border_radius="10px"
            ),
            on_click=rx.redirect(path=url, is_external=is_external)
        ),
        background_color= styles.PageColor.EXTRA_LIGHT.value,
        variant="ghost",
        as_child=True
        
    )
