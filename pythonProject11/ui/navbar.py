import reflex as rx
from pythonProject11 import navigation
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def base_navbar(*args,**kwargs,) -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://media.licdn.com/dms/image/D560BAQHd5luGIhmcow/company-logo_200_200/0/1710703863813/reflex_dev_logo?e=2147483647&v=beta&t=8lFxQEmRQUID9smd9kXAl8_cPwHRrSRzViQb2izipf8",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex-Chat", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("Chat", "/chats"),

                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://media.licdn.com/dms/image/D560BAQHd5luGIhmcow/company-logo_200_200/0/1710703863813/reflex_dev_logo?e=2147483647&v=beta&t=8lFxQEmRQUID9smd9kXAl8_cPwHRrSRzViQb2izipf8",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex-GPT", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigation.state.NavState.to_home),
                        rx.menu.item("About", on_click=navigation.state.NavState.to_about),
                        rx.menu.item("Chat", on_click=navigation.state.NavState.to_chat),

                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",

            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="1px",
        z_index="5",
        width="100%",
        height="70px",
        left="1px",
        right="1px",


        *args,  # Pass content from other pages here
        **kwargs,
    )