from flet import *
from gui.pages.start_page import Start
from gui.pages.welcome_page import Welcome
from gui.pages.food_build_page import FoodBuild


def main(page: Page):
    page.title = "Legourmet"
    page.window_resizable = True
    page.padding = 0
    page.window_max_height = 720
    page.window_max_width = 1280
    page.window_width = 1280
    page.window_height = 720
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ThemeMode.SYSTEM

    # pages
    start_page = Start(page)
    welcome_page = Welcome(page)
    food_build = FoodBuild(page)

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                View(
                    route="/",
                    controls=[start_page.main()],
                )
            )
        elif page.route == "/welcome_page":
            welcome_page.start_processing()
            page.views.append(
                View(
                    route="/welcome_page",
                    controls=[welcome_page.main()],
                )
            )
        elif page.route == "/food_build_page":
            page.views.append(
                View(
                    route="/food_build_page",
                    controls=[food_build.main()],
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")


if __name__ == "__main__":
    app(target=main)
