from flet import *
import os
import sys
import threading
import cv2
import time
import base64
from gui.resources.resources_path import ImagePaths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class InputFood:
    def __init__(self, page):
        super().__init__()
        self.cap = None
        self.capture = None
        self.page = page
        self.images = ImagePaths()
        self.image_control = Image(src=self.images.bot_img, width=640, height=480)
        self.running = False

    def main(self):
        legourmet_watermark = Text(
            value="Legourmet by Geniiia", font_family='Poppins', size=10, color='#FFFFFF')

        text_title = Text("¡Dale vida a tu creación!", size=72, weight='bold', color='#FF6F61', font_family='Poppins')

        text_instruction = Text("Una vez estés conforme con tu creación ingresa tu tablero a nuestro sistema para "
                                "darle vida a tu plato.", size=24, color='#FFFFFF')

        text_button = Text("ARMA TU PLATO", size=24, color='#008F5C', weight='bold', font_family='Poppins')

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
                            text_title
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_instruction
                        ], alignment='center'
                    ),
                    Row(
                        [
                            Container(
                                content=ElevatedButton(
                                    content=text_button, on_click=self.video_capture, bgcolor='#00FFA3'
                                ), padding=padding.symmetric(horizontal=10, vertical=10), border_radius=20,
                                alignment=alignment.center_right, expand=True
                            )
                        ]
                    ),
                    Row(
                        [
                            Card(
                                content=Container(
                                    self.image_control,
                                    padding=0,
                                    border_radius=10,
                                    bgcolor='white',
                                    shadow=BoxShadow(
                                        blur_radius=10,
                                        spread_radius=5,
                                        color='rgba(0, 0, 0, 0.2)'
                                    ),
                                    expand=True
                                ),
                                width=640,
                                height=480,
                                margin=margin.all(10),
                                elevation=5
                            )
                        ],
                        alignment='center',
                        expand=True
                    ),

                ],
                alignment='center',
                spacing=10
            ), gradient=gradient, expand=True, padding=padding.all(20), width=self.page.window_width,
            height=self.page.window_height,
        )
        return elements

    def video_capture(self, e):
        self.start_webcam()

    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.running = True
        threading.Thread(target=self.update_frame, daemon=True).start()

    def stop_webcam(self):
        self.running = False
        if self.capture:
            self.capture.release()
        self.image_control.src = self.images.bot_img
        self.page.update()

    def update_frame(self):
        while self.running:
            ret, frame = self.capture.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            self.image_control.src_base64 = jpg_as_text
            self.page.update()
            time.sleep(0.03)

    def on_close(self):
        if self.cap:
            self.cap.release()
