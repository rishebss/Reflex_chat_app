import reflex as rx
from . navbar import base_navbar
from .footer import base_footer

def base_layout(*args, **kwargs) -> rx.Component:
    """Defines the base layout with the navbar."""
    return rx.container(
        base_navbar(),
        rx.fragment(
        *args,
            **kwargs,
        ),






    )
