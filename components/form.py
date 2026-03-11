import reflex as rx
from styles import styles

def form() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(placeholder="First Name", name="fist_name", 
                             background_color=styles.PageColor.EXTRA_LIGHT.value),
                    rx.input(placeholder="Last Name", name="last_name",
                             background_color=styles.PageColor.EXTRA_LIGHT.value,),
                    width=styles.TOTAL_WIDTH,
                    
                ),
                rx.input(placeholder="e-mail", 
                         name="mail", 
                         type="email", 
                         required=True,
                         width=styles.TOTAL_WIDTH,
                         background_color=styles.PageColor.EXTRA_LIGHT.value),
                rx.input(placeholder="Message", 
                         name="mensaje",
                         max_length=800,
                         width=styles.TOTAL_WIDTH,
                         height="auto",
                         min_height="200px",
                         background_color=styles.PageColor.EXTRA_LIGHT.value),
                rx.box(
                    rx.hstack(
                        rx.checkbox("Send", name="send"),
                        rx.button("Submit", type="submit"),
                        align="center"
                    ),
                    width=styles.TOTAL_WIDTH,
                    display="flex",
                    justify_content="center"
                )
            ),
            width=styles.TOTAL_WIDTH
        ),
        width=styles.TOTAL_WIDTH
    )