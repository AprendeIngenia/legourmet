from flet import *
from gui.resources.resources_path import (ImagePaths, FontsPath)


class Start:
    def __init__(self, page):
        super().__init__()
        self.images = ImagePaths()
        self.fonts = FontsPath()

        self.page = page
        self.page.fonts = {
            "Brittany": self.fonts.brittany_font,
            "Cardo": self.fonts.cardo_font
        }

    def main(self):
        tapas_text = Text(
            "Tapas",
            font_family="Brittany",
            size=48,
            weight='bold',
            color='#FFFFFF'
        )

        carnes_quesos_text = Text(
            "Carnes y quesos",
            font_family='Cardo',
            size=60,
            weight='bold',
            color='#DB7024'
        )
        madurados_text = Text(
            "madurados",
            font_family='Cardo',
            size=60,
            weight='bold',
            color='#DB7024'
        )
        start_button = ElevatedButton(
            text="Inicio",
            on_click=self.start,
            bgcolor='#DB7024',
            color='#FFFFFF',
            width=180,
            height=40,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10)
            )
        )

        carnes_image = Image(src=self.images.image_1, width=252, height=800, fit=ImageFit.COVER)
        quesos_image = Image(src=self.images.image_2, width=252, height=800, fit=ImageFit.COVER)
        toppings_image = Image(src=self.images.image_3, width=252, height=800, fit=ImageFit.COVER)

        carnes_column = Stack(
            [
                carnes_image,
                Text("Carnes", font_family="Brittany", size=48, color='#FFFFFF', offset=Offset(0.5, -0.55)),
            ],
            width=252,
            height=800
        )

        quesos_column = Stack(
            [
                quesos_image,
                Text("Quesos", font_family="Brittany", size=48, color='#FFFFFF', offset=Offset(0.5, -0.55)),
            ],
            width=252,
            height=800
        )

        toppings_column = Stack(
            [
                toppings_image,
                Text("Toppings", font_family="Brittany", size=48, color='#FFFFFF', offset=Offset(0.5, -0.55)),
            ],
            width=252,
            height=800
        )

        left_column = Column(
            controls=[
                tapas_text,
                carnes_quesos_text,
                madurados_text,
                start_button
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=0
        )

        elements = Container(
            content=Row(
                controls=[
                    left_column,
                    carnes_column,
                    quesos_column,
                    toppings_column
                ],
                alignment='spaceEvenly',
                vertical_alignment='center',
            ),
            bgcolor='#0E0E0E',
            padding=0,
            expand=True
        )
        return elements

    def start(self, e):
        self.page.go("/welcome_page")
