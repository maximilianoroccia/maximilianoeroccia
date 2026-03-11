import reflex as rx
from components import link_button, title
from styles import styles

def links() -> rx.Component:
    return rx.vstack(
        title("Links de interes"),
        link_button(
            "Resumen actualizado",
            "Accede a un CV actualizado a día de hoy",
            "/icons/pdf.svg",
            "tucasa.com"
        ),
        link_button(
            "LinkedIn",
            "Ve a mi red profesional por info",
            "/icons/linkedIn.svg",
            "https://www.linkedin.com/in/maximiliano-e-roccia/"
        ),
        link_button(
            "Proyectos",
            "Conoce más de mis proyectos",
            "/icons/hammer.svg",
            "/proyects",
            is_external= False
        ),
        link_button(
            "Blog",
            "Charlas sobre tecnología y más",
            "/icons/blog.svg",
            "/blog",
            is_external= False
        ),
        spacing=styles.Spacings.MEDIUM_SMALL.value,
        width=styles.TOTAL_WIDTH
    )
