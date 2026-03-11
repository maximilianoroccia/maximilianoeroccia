import reflex as rx
from styles import Sizes, Spacings, Font, FontWeight, PageColor, TextColor, NumSize

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.text("Maxi", weight="bold", size="5", color=TextColor.BLUE),
                rx.text("Emb", weight="bold", size="5", color=TextColor.GREEN),
                rx.text("Dev", weight="bold", size="5", color=TextColor.BLUE),
                spacing=Spacings.ZERO.value
                
            ),
            href="/"
        ),
        position="sticky",
        bg=PageColor.PRIMARY,
        padding_x=Sizes.DEFAULT.value,
        padding_y=Sizes.XSMALL.value,
        margin_bottom=Sizes.SMALL.value,
        weight=NumSize.SMALL.value,
        z_index="999", 
    )
    