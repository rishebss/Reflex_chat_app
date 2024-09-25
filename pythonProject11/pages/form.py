import reflex as rx
from .state import ChatState

def chat_form() -> rx.Component:
    return rx.form(
        rx.hstack(  # Horizontal stack for text area and button
            rx.text_area(
                name='message',
                placeholder="Your Message",
                required=True,
                width="100%",  # Full width for the text area
            ),
            rx.button(
                "Submit",
                type='submit',
                bg=rx.color("accent", 3),
                height="60px",  # Set the height of the button
            ),
            justify_content="space-between",  # Space between text area and button
            align_items="center",  # Vertically center text area and button
            width="100%",  # Ensure the container takes full width
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=True,
        style={
            "position": "fixed",  # Fixes the position
            "bottom": "0",  # Aligns to the bottom of the page
            "left": "0",  # Aligns to the left
            "right": "0",  # Aligns to the right
            "backgroundColor": "black",  # Optional: set a background color
            "padding": "10px",  # Optional: padding for spacing
            "boxShadow": "0 -2px 5px rgba(0, 0, 0, 0.1)",  # Optional: shadow for separation
        }
    )



