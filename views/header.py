import reflex as rx
from styles import Sizes, Spacings, Font, FontWeight, PageColor, TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Maximiliano Roccia"),
            rx.hstack(
                rx.text("Maxi", height=FontWeight.MEDIUM, color=TextColor.BLUE),
                rx.text("Emb", height=FontWeight.MEDIUM, color=TextColor.GREEN),
                rx.text("Dev", height=FontWeight.MEDIUM, color=TextColor.BLUE),
                spacing=Spacings.ZERO.value
            )
        ),
        rx.text("Hola mi nombre es Maxi Roccia", color=TextColor.LIGHT),
        rx.text("""Soy ingeniero de software y hardware desde hace más de 5 años.
                Actualmente trabajo como freelancer en desarrollos end to end,
                creando sistemas y servicios con sistemas embedidos desde el chip
                hasta la web de visualizacion. ¡Bienvenidos!""", color=TextColor.LIGHT),
        rx.avatar(fallback= "MED", size="5")     
    )
