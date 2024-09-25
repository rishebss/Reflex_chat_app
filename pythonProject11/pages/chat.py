import reflex as rx
from pythonProject11 import ui
from .form import chat_form
from .state import ChatMessage
from .state import ChatState

message_style = dict(
    display="inline-block",
    padding="1em ",
    border_radius="8px",
    max_width=["30em","30em","50em","50em","50em","50em"],
    left="1px",
    right="1px",


)




def message_box(chat_message: ChatMessage) -> rx.Component:
    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(chat_message.is_bot, rx.color("mauve", 4), rx.color('blue', 4)),
                color=rx.cond(chat_message.is_bot, rx.color('mauve', 12), rx.color("blue", 12)),
                **message_style,

            ),
            text_align=rx.cond(chat_message.is_bot, "left", "right"),
            margin_top="1em",
            margin_bottom="2em"



        ),
     width = "100%",





    )

# def message_box(chat_message:ChatMessage):
#     return rx.box(
#
#         rx.text(chat_message.message),
#         background_color=rx.cond(chat_message.is_bot,rx.color('gray'),rx.color('accent',3))
#     )

def chat_page() -> rx.Component:

    return ui.base_layout(
        rx.vstack(
                rx.heading(
                "",
                size="9"),
                rx.box(
                    rx.foreach(ChatState.messages,message_box),
                    width="100%",


                    border_radius="8px"
                ),
                chat_form(),
                margin="3rem auto",
                spacing="5",
                justify="center",
                min_height="85vh",

        )
    )