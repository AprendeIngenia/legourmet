from flet import *
import os
import sys
from gui.resources.resources_path import (ImagePaths, FontsPath)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class InputFood:
    def __init__(self, page, shared_data):
        super().__init__()
        self.images = ImagePaths()
        self.fonts = FontsPath()

        self.page = page
        self.shared_data = shared_data
        self.page.fonts = {
            "Brittany": self.fonts.brittany_font,
            "Cardo": self.fonts.cardo_font
        }

    def main(self):
        title = Text("Ingresa la base", font_family="Brittany", size=48, color='#FFFFFF', weight='bold')

        step1_tittle = Text("Paso 1:", font_family='Brittany', size=48, color='#DB7024', weight='bold')
        step2_tittle = Text('Paso 2:', font_family='Brittany', size=48, color='#DB7024', weight='bold')
        step3_tittle = Text('Paso 3:', font_family='Brittany', size=48, color='#DB7024', weight='bold')

        step1_description = Text("Identifica la ranura que tengo en la parte baja de mi cuerpo.",
                                 font_family="Cardo", size=24,
                                 color='#FFFFFF')
        step2_description = Text("Ingresa la base de construcción en la ranura.",
                                 font_family="Cardo", size=24,
                                 color='#FFFFFF')
        step3_description = Text("Aqui puedes verificar si has ingresado correctamente tu base.",
                                 font_family="Cardo", size=24,
                                 color='#FFFFFF')

        step1_image = Image(src=self.images.image_8, width=300, height=420, fit=ImageFit.COVER)
        step2_image = Image(src=self.images.image_9, width=360, height=420, fit=ImageFit.COVER)

        progress_label = Text("75%", size=20, weight=FontWeight.BOLD)
        progress_bar = ProgressBar(value=0.75, width=300, color="#DB7024")

        left_column = Column(
            controls=[
                step1_tittle,
                Container(step1_description, width=400),
                step1_image
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=20,
            expand=True
        )
        center_column = Column(
            controls=[
                title,
                Container(height=730),
                step3_tittle,
                Container(step3_description, width=400),
                progress_bar,
                progress_label
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=20,
            expand=True
        )

        right_column = Column(
            controls=[
                step2_tittle,
                Container(step2_description, width=400),
                step2_image
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
                    center_column,
                    right_column,
                ],
                alignment='center',
                vertical_alignment='start',
            ),
            bgcolor='#0E0E0E',
            padding=padding.all(50),
            expand=True
        )
        return elements

    def create_food_plate(self, e):
        self.page.go("/confirmated_food_page")
