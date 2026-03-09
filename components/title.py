import reflex as rx
from styles import TextColor

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        color = TextColor.LIGHT.value
    )