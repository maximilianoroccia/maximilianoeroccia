import reflex as rx
from styles import Sizes, Spacings, Font, FontWeight, PageColor, TextColor, styles

def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.text("Maxi", weight="bold", size="5", color=TextColor.BLUE),
                rx.text("Emb", weight="bold", size="5", color=TextColor.GREEN),
                rx.text("Dev", weight="bold", size="5", color=TextColor.BLUE),
                spacing=Spacings.ZERO.value,
            ),
            rx.text("Hola mi nombre es Maxi Roccia", color=TextColor.LIGHT),
            rx.text("""Soy ingeniero de software y hardware desde hace más de 5 años.
                Actualmente trabajo como freelancer en desarrollos end to end,
                creando sistemas y servicios con sistemas embedidos desde el chip
                hasta la web de visualizacion. ¡Bienvenidos!""", color=TextColor.LIGHT),
        ),
        rx.avatar(
            fallback= "MED", 
            size=styles.NumSize.BIG.value,
            src="/perfil_web.png"), 
        width=styles.MAX_WIDTH,
        align_items="center"
        
    )
