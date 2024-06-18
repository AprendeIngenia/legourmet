import os
import sys
import threading
import time
from flet import *
from frame_process.processor import PeopleProcessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class Welcome:
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.frame_processor = PeopleProcessing()
        self.people_count_text = Text("", font_family='Poppins', size=40, color='#00FFA3', weight='bold')
        self.food_plates_input = TextField(adaptive=True, on_change=self.manual_people_count_change)
        self.auto_detect_people_switch = Switch(label="Auto detectar", value=True, on_change=self.toggle_processing)
        self.processing_thread = None

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
            while self.auto_detect_people_switch.value:
                number_people = self.get_people_count()
                self.people_count_text.value = f'Vemos que nos acompañan {number_people} visitantes.'
                self.food_plates_input.label = f'¿Desean ordenar {number_people} platos?'
                self.food_plates_input.value = number_people
                self.page.update()
                time.sleep(1)

        self.processing_thread = threading.Thread(target=update, daemon=True)
        self.processing_thread.start()

    def toggle_processing(self, e):
        if self.auto_detect_people_switch.value:
            self.start_processing()
        else:
            self.stop_processing()

    def manual_people_count_change(self, e):
        # Desactivar auto detección cuando el usuario cambie el valor manualmente
        self.auto_detect_people_switch.value = False
        self.stop_processing()
        self.page.update()

    def main(self):

        legourmet_watermark = Text(
            value="Legourmet by Geniiia", font_family='Poppins', size=10, color='#FFFFFF')

        text_welcome = Text("¡Bienvenidos a Legourmet!", font_family='Poppins', size=72, weight='bold', color='#FF7F50')

        text_2 = Text("el único restaurante dirigido por inteligencia artificial.", size=20,
                      color='#FFFFFF', font_family='Open sans')

        text_3 = Text("Antes de empezar con la experiencia indicanos el número de platos que deseas ordenar:", size=20,
                      color='#FFFFFF', font_family='Open sans')

        plates_button = Container(
            content=ElevatedButton(
                content=Container(
                    content=Column(
                        [Text(value="ORDENAR", size=24, color='#008F5C', weight='bold',
                              font_family='Poppins')],
                        alignment=MainAxisAlignment.CENTER, spacing=3),
                    padding=padding.all(8)),
                on_click=self.number_food_plates, bgcolor='#00FFA3'),
            padding=padding.symmetric(horizontal=2, vertical=2),
            border_radius=20)

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
                            text_welcome
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_2
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_3
                        ], alignment='center'
                    ),
                    Row(
                        [
                            self.people_count_text
                        ], alignment='center'
                    ),
                    Row(
                        [
                            self.food_plates_input,
                            self.auto_detect_people_switch
                        ], alignment='center'
                    ),
                    Row(
                        [
                            plates_button
                        ], alignment='center'
                    )
                ]
            ), gradient=gradient, expand=True
        )
        return elements

    def number_food_plates(self, e):
        num_plates = self.food_plates_input.value
        self.page.go("/food_build_page")
        self.stop_processing()
