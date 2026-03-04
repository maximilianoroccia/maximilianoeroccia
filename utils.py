import reflex as rx

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")

preview = "preview.png"
autor = "MaxiEmbDev"
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "author", "content": autor}
]

# INDEX PAGE

index_title = f"Welcome to {autor} Portfolio"
index_description = "Explore my projects and skills in web development and design."
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)

# PROYECTS PAGE

proyects_title = f"{autor} Proyects"
proyects_description = "Discover the web development projects I've worked on, showcasing my skills and creativity."
proyects_meta = [
    {"name": "og:title", "content": proyects_title},
    {"name": "og:description", "content": proyects_description}   
]
proyects_meta.extend(_meta)

# BLOG PAGE

blog_title = f"{autor} Blog"
blog_description = "News and interesting articles about embedded systems and programming"
blog_meta = [
    {"name": "og:title", "content": blog_title},
    {"name": "og:description", "content": blog_description}   
]
blog_meta.extend(_meta)



