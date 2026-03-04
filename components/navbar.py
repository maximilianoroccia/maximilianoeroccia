import reflex as rx
from styles import Sizes, Spacings, Font, FontWeight, PageColor, TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.text("Maxi", height=FontWeight.MEDIUM, color=TextColor.BLUE),
                rx.text("Emb", height=FontWeight.MEDIUM, color=TextColor.GREEN),
                rx.text("Dev", height=FontWeight.MEDIUM, color=TextColor.BLUE),
                spacing=Spacings.ZERO.value
            ),
            href="/"
        ),
        position="sticky",
        bg=PageColor.PRIMARY,
        padding_x=Sizes.DEFAULT.value,
        padding_y=Sizes.SMALL.value,
        z_index="999", 
    )