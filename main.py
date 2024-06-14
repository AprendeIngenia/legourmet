from flet import *
import cv2

from flet import *
import flet
from gui.pages.page_routes import route_change, on_route_change, on_view_pop


def main(page: Page):
    page.window_resizable = True
    page.padding = 0
    page.window_max_height = 720
    page.window_max_width = 1280
    page.window_width = 1280
    page.window_height = 720
    page.theme_mode = ThemeMode.SYSTEM

    page.on_route_change = on_route_change(page)
    page.on_view_pop = on_view_pop(page)
    page.go("/")


app(main)
