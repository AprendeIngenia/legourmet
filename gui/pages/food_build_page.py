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
                                font_family="Cardo", size=24,
                                color='#FFFFFF', text_align="justify")

        understood_button = ElevatedButton(
            text="Entendido",
            bgcolor='#DB7024',
            color='#FFFFFF',
            width=180,
            height=40,
            on_click=self.create_food_plate,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10)
            )
        )

        step1_tittle = Text('Paso 1:', font_family='Brittany', size=48, color='#FFFFFF', weight='bold')
        step2_tittle = Text('Paso 2:', font_family='Brittany', size=48, color='#FFFFFF', weight='bold')
        step3_tittle = Text('Paso 3:', font_family='Brittany', size=48, color='#FFFFFF', weight='bold')
        step1_description = Text("Toma la base de la mesa e identifica la zona de construcción demarcada con un "
                                 "rectángulo naranja.",
                                 font_family="Cardo", size=24,
                                 color='#FFFFFF')
        step2_description = Text("En esta zona debes ubicar las fichas que representan los deliciosos ingredientes "
                                 "que manejamos en tapas.",
                                 font_family="Cardo", size=24,
                                 color='#FFFFFF')
        step3_description = Text("Configuralos hasta sentir que has creado tu plato perfecto.",
                                 font_family="Cardo", size=24,
                                 color='#FFFFFF')

        step1_image = Image(src=self.images.image_5, width=200, height=200, fit=ImageFit.COVER)
        step2_image = Image(src=self.images.image_6, width=200, height=200, fit=ImageFit.COVER)
        step3_image = Image(src=self.images.image_7, width=200, height=200, fit=ImageFit.COVER)

        step1 = Row(
            controls=[
                step1_tittle,
                Container(content=step1_description, width=800)
            ], alignment='center',
            spacing=20
        )
        step2 = Row(
            controls=[
                step2_tittle,
                Container(content=step2_description, width=800)
            ], alignment='center',
            spacing=20
        )
        step3 = Row(
            controls=[
                step3_tittle,
                Container(content=step3_description, width=800)
            ], alignment='center',
            spacing=20
        )

        left_column = Column(
            controls=[
                food_build_text,
                Container(description_text, width=400),
                Container(height=40),
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

        right_column = Column(
            controls=[
                step1,
                step1_image,
                step2,
                step2_image,
                step3,
                step3_image
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=30,
            expand=True
        )

        elements = Container(
            content=Row(
                controls=[
                    Container(left_column, width=400),
                    Container(right_column, width=950),
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
