from flet import *
import os
import sys
from gui.resources.resources_path import (ImagePaths, FontsPath)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class FoodBuild:
    def __init__(self, page, shared_data):
        self.images = ImagePaths()
        self.fonts = FontsPath()

        self.page = page
        self.shared_data = shared_data
        self.page.fonts = {
            "Brittany": self.fonts.brittany_font,
            "Cardo": self.fonts.cardo_font
        }

    def main(self):
        food_build_text = Text("Construye tu plato", font_family="Brittany", size=48, color='#FFFFFF', weight='bold')
        description_text = Text("Hoy conocerás la experiencia más innovadora que jámas hayas vivido en la historia de "
                                "la gastronomía. Abre tu mente, y prepárate para disfrutar de unas deliciosas Tapas.",
                                font_family="Cardo", size=20,
                                color='#FFFFFF')
        understood_button = ElevatedButton(
            text="Aceptar",
            bgcolor='#DB7024',
            color='#FFFFFF',
            width=180,
            height=40,
            on_click=self.create_food_plate,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10)
            )
        )

        left_column = Column(
            controls=[
                food_build_text,
                description_text,
                Row(
                    controls=[
                        understood_button,
                    ],
                    alignment='center',
                    spacing=20
                )
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=20,
            expand=True
        )

        elements = Container(
            content=Row(
                controls=[
                    left_column,
                ],
                alignment='spaceBetween',
                vertical_alignment='center',
            ),
            bgcolor='#0E0E0E',
            padding=padding.all(50),
            expand=True
        )
        return elements

    def create_food_plate(self, e):
        self.page.go("/food_input_page")
