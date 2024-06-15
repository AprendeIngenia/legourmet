from flet import *
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gui.resources.resources_path import ImagePaths


class FoodBuild:
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.images = ImagePaths()

    def main(self):
        legourmet_watermark = Text(
            value="Legourmet by Geniiia", font_family='Poppins', size=10, weight='bold', color='#FFFFFF')

        text_build = Text("¡Construye tu plato!", size=72, weight='bold', color='#00FFA3', font_family='Poppins')

        text_2 = Text("Agrega un bloque que representa un ingrediente.", size=24, color='#FFFFFF', font_family='Poppins')

        text_3 = Text("Configuralos hasta sentir que has creado tu plato perfecto", size=24, color='#FFFFFF',
                      font_family='Poppins')

        img_brick = Image(src=self.images.brick_img, width=80, height=80)
        arrow = Text("→", size=48, color='#FFFFFF')
        img_tapas = Image(src=self.images.tapas_img, width=80, height=80)

        img_bricks = Image(src=self.images.bricks_img, width=80, height=80)
        img_plate = Image(src=self.images.plate_img, width=80, height=80)

        gradient = LinearGradient(
            begin=alignment.top_left, end=alignment.bottom_right, colors=['#0B0B24', '#1A1C1E'])

        elements = Container(
            content=Column(
                [
                    Row(
                        [
                            legourmet_watermark
                        ], alignment='start'
                    ),
                    Row(
                        [
                            text_build
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_2
                        ], alignment='center'
                    ),
                    Row(
                        [
                            img_brick,
                            arrow,
                            img_tapas
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_3
                        ], alignment='center'
                    ),
                    Row(
                        [
                            img_bricks,
                            arrow,
                            img_plate
                        ], alignment='center'
                    )
                ]
            ), gradient=gradient, expand=True
        )
        return elements
