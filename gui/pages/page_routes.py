from flet import *
from gui.pages.start_page import Start
from gui.pages.welcome_page import Welcome


def route_change(page, route):
    views = {
        "/": Start(page).main(),
        "/welcome_page": Welcome(page).main(),
    }
    return views.get(route, Start(page).main())


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
