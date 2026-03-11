import reflex as rx
from components import card_proyects, title
from styles import Sizes, Spacings, Font, FontWeight, PageColor, TextColor, styles

def proy_index() -> rx.Component:
    return rx.vstack(
        title("Proyectos destacados"),
        card_proyects(
            "iNVERMAX",
            "invermax.com",
            "invermax.png",
            """Sistema de control y monitoreo de invernaderos autonomo 
            con dashboard web con autenticación multinivel y 
            actualizaciones OTA""",
        ),
        card_proyects(
            "Greenest Manager System",
            "greenest.com",
            "greenest.png",
            """Producto IoT embebidos para monitoreo, recolección y 
            procesamiento de datos en remoto para gestion integral de real
            state y cumplimiento de normativas 2030 sobre sostenibilidad y gobernanza""",
        ),
        margin_y=styles.Sizes.XSMALL.value,
        spacing_y=styles.Spacings.MEDIUM_SMALL.value,
        justify_content="start"
    )