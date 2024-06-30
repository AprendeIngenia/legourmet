from flet import *
from gui.pages.start_page import Start
from gui.pages.welcome_page import Welcome
from gui.pages.food_build_page import FoodBuild
from gui.pages.food_input_page import InputFood


class MainApp:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Legourmet"
        self.page.bgcolor = "#0E0E0E"
        self.page.window_resizable = False
        self.page.padding = 0
        self.page.window_width = 1536
        self.page.window_height = 2048
        self.page.vertical_alignment = "center"
        self.page.horizontal_alignment = "center"

        self.page.theme = Theme(
            page_transitions=PageTransitionsTheme(
                android=PageTransitionTheme.FADE_UPWARDS,
                ios=PageTransitionTheme.CUPERTINO,
                macos=PageTransitionTheme.ZOOM,
                linux=PageTransitionTheme.ZOOM,
                windows=PageTransitionTheme.FADE_UPWARDS,
            ),
        )

        self.shared_data = {}

        self.start_page = Start(page)
        self.welcome_page = Welcome(page, self.shared_data)
        self.food_build_page = FoodBuild(page, self.shared_data)
        self.input_food_page = InputFood(page, self.shared_data)

        self.page.on_route_change = self.route_change
        self.page.go("/")

    def route_change(self, route):
        self.page.views.clear()
        if self.page.route == "/":
            self.page.views.append(
                View(
                    route="/",
                    controls=[self.start_page.main()],
                )
            )
        elif self.page.route == "/welcome_page":
            self.welcome_page.start_processing()
            self.page.views.append(
                View(
                    route="/welcome_page",
                    controls=[self.welcome_page.main()],
                )
            )
        elif self.page.route == "/food_build_page":
            self.page.views.append(
                View(
                    route="/food_build_page",
                    controls=[self.food_build_page.main()],
                )
            )
        elif self.page.route == "/food_input_page":
            self.page.views.append(
                View(
                    route="/food_input_page",
                    controls=[self.input_food_page.main()],
                )
            )
        self.page.update()


def main(page: Page):
    MainApp(page)


if __name__ == "__main__":
    app(target=main)
