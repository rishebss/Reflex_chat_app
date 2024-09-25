import reflex as rx
from pythonProject11 import ui,navigation
from rxconfig import config


def home_page() -> rx.Component:
    # Page with a welcome message
    return ui.base_layout(  # Use the base layout with navbar
        rx.vstack(
            rx.box(
                rx.text(
                    "Welcome to the Homepage! Please use the chat bot",
                    font_size="24px",
                    font_weight="bold",
                    padding="20px",
                    margin_top="100px",

                ),  # Welcome message
                rx.hstack(  # Horizontal stack for centering
                    rx.button(
                        "Reflex-Chat",
                        on_click=navigation.state.NavState.to_chat,
                        bg=rx.color("accent", 3),
                        height="40px",  # Set the height of the button
                        border_radius="10px"
                    ),
                    justify_content="center",  # Center the button horizontally
                    width="100%",  # Full width to ensure centering
                ),

            ),

        ),

    )




