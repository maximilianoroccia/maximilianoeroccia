import reflex as rx
import pages as pg
from fastapi import FastAPI
from rxconfig import config
from styles import styles


fastapi_app = FastAPI()
app = rx.App(
    style=styles.BASE_STYLE,
    api_transformer=[fastapi_app]
)

app.add_page(pg.index , route="/")
app.add_page(pg.proyects, route="/proyectos")
app.add_page(pg.blog, route="/blog")

