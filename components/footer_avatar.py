import reflex as rx
from styles import styles

def footer_avatar(image: str, url_site:str) -> rx.Component:
    return rx.avatar(
        rx.link(url=url_site),
        src=image,
        variant="soft",
        radius="small",
        size=styles.NumSize.MEDIUM.value        
    )