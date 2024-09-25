import reflex as rx
from pythonProject11 import ui

def chat_page() -> rx.Component:

    return ui.base_layout(
        rx.vstack(
                rx.heading(
                "chats here",
                size="9"),
                spacing="5",
                justify="center",
                min_height="85vh",

        )
    )