import os
import sys
import threading
import time
from flet import *
from frame_process.processor import PeopleProcessing
from gui.resources.resources_path import (ImagePaths, FontsPath)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class Welcome:
    def __init__(self, page, shared_data: dict):
        self.images = ImagePaths()
        self.fonts = FontsPath()

        self.frame_processor = PeopleProcessing()

        self.page = page
        self.shared_data = shared_data
        self.page.fonts = {
            "Brittany": self.fonts.brittany_font,
            "Cardo": self.fonts.cardo_font
        }

        self.people_count_text = Text("", font_family='Cardo', size=20, color='#FFFFFF')
        self.food_plates_input = TextField(label="", width=200, text_size=20, color='#FFFFFF', border_color='#DB7024',
                                           border_radius=10, on_change=self.manual_people_count_change)
        self.processing_thread = None
        self.ia_process: bool = True

    def start_processing(self):
        self.frame_processor.start_processing()
        self.update_people_count()

    def stop_processing(self):
        self.frame_processor.stop_processing()
        if self.processing_thread:
            self.processing_thread = None

    def get_people_count(self):
        return self.frame_processor.get_people_count()

    def update_people_count(self):
        def update():
            while self.ia_process:
                number_people = self.get_people_count()
                if number_people == 1:
                    self.people_count_text.value = f'Vemos que nos acompaña {number_people} visitante'
                    self.food_plates_input.label = f'¿Deseas ordenar {number_people} plato?'
                else:
                    self.people_count_text.value = f'Vemos que nos acompañan {number_people} visitantes'
                    self.food_plates_input.label = f'¿Desean ordenar {number_people} platos?'
                self.food_plates_input.value = number_people
                self.page.update()
                time.sleep(0.1)

        self.processing_thread = threading.Thread(target=update, daemon=True)
        self.processing_thread.start()

    def manual_people_count_change(self, e):
        self.people_count_text.value = f'Por favor ingresa el numero de platos que deseas ordenar'
        self.food_plates_input.label = f'Ingresa numero de platos'
        if self.ia_process:
            self.food_plates_input.value = ""
        self.ia_process = False
        self.stop_processing()
        self.page.update()

    def main(self):
        self.start_processing()
        tapas_image = Image(src=self.images.image_4, width=520, height=1238, fit=ImageFit.COVER)
        tapas_text = Text(
            "Tapas",
            font_family="Brittany",
            size=48,
            weight='bold',
            color='#FFFFFF',
            offset=Offset(2.15, -0.55)
        )

        welcome_text = Text("Bienvenidos", font_family="Brittany", size=48, color='#FFFFFF', weight='bold')
        description_text = Text("Descubre las mejores tapas ibéricas de la ciudad.", font_family="Cardo", size=20,
                                color='#FFFFFF')

        start_button = ElevatedButton(
            text="Aceptar",
            bgcolor='#DB7024',
            color='#FFFFFF',
            width=180,
            height=40,
            on_click=self.number_food_plates,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10)
            )
        )

        cancel_button = ElevatedButton(
            text="Declinar",
            bgcolor='#A9A9A9',
            color='#FFFFFF',
            width=180,
            height=40,
            on_click=self.manual_people_count_change,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10)
            )
        )

        left_column = Stack(
            [
                tapas_image,
                tapas_text,
            ],
            width=520,
            height=1238,
            alignment=Alignment(-1, 0)
        )

        right_column = Column(
            controls=[
                welcome_text,
                description_text,
                self.people_count_text,
                self.food_plates_input,
                Row(
                    controls=[
                        start_button,
                        cancel_button
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
                    right_column
                ],
                alignment='spaceBetween',
                vertical_alignment='center',
            ),
            bgcolor='#0E0E0E',
            padding=padding.all(50),
            expand=True
        )

        return elements

    def number_food_plates(self, e):
        self.shared_data['number_plates_food'] = self.food_plates_input.value
        self.page.go("/food_build_page")
        self.stop_processing()
