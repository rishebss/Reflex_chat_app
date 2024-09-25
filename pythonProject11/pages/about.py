import reflex as rx
from pythonProject11 import ui

def about_page() -> rx.Component:
    # About Page
    return ui.base_layout(  # Use the base layout with navbar
        rx.container(
            rx.heading("About Us", size="9", justify="center", margin_top="300px"),
        ),
    )