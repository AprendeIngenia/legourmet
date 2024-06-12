from flet import *
from gui.pages.home import Home
from gui.pages.page2 import Page2
from gui.pages.captureTest import CaptureTest

def route_change(page, route):
    views = {
        "/": Home(page).build(),
        "/page2": Page2(page).build(),
        "/captureTest": CaptureTest(page).build(),
    }
    return views.get(route, Home(page).build())

def on_route_change(page):
    def handler(e):
        page.views.clear()
        page.views.append(
            View(
                route=page.route,
                controls=[route_change(page, page.route)]
            )
        )
        page.update()
    return handler

def on_view_pop(page):
    def handler(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    return handler