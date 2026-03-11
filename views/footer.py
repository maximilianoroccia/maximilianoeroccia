import reflex as rx
from styles import styles
from components import footer_avatar

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(" Todos los derechos reservados ® 2026, pero echo con cariño para que revises sobre mi"),
        rx.text("Tecnologías que uso a diario"),
        rx.flex(
            footer_avatar("/favicon.ico", "reflex.dev"),
            footer_avatar("icons/python.svg", "python.org"),
            footer_avatar("/icons/c-logo.svg", "isocpp.org"),
            spacing="2"
        ),
        justify_content="center"
    )