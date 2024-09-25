import reflex as rx
from. import pages,navigation
from rxconfig import config
from. import ui,chats



app = rx.App(
    layout=ui.base_layout  # Apply the base layout to all pages
)

app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE)
app.add_page(pages.chat_page, route=navigation.routes.CHAT_ROUTE)

