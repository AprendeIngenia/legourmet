import cv2
from flet import *
import threading
import time
import base64

class CaptureTest(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.capture = None
        # Inicializar con una imagen predeterminada desde el directorio de assets
        self.image_control = Image(src="/assets/icono.png", width=640, height=480)
        self.running = False

    def start_webcam(self):
        self.capture = cv2.VideoCapture(1)
        self.running = True
        threading.Thread(target=self.update_frame, daemon=True).start()

    def stop_webcam(self):
        self.running = False
        if self.capture:
            self.capture.release()
        self.image_control.src = "/assets/icono.png"
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
            time.sleep(0.03)  # Control the frame rate

    def build(self):
        return Container(
            Column([
                Text("LEGOURMET", size=24, weight='bold', color='white'),
                Text("Test de camara.", size=16, color='white'),
                Card(
                    content=Container(
                        self.image_control,
                        padding=10,
                        border_radius=10,
                        bgcolor='white',
                        shadow=BoxShadow(
                            blur_radius=10,
                            spread_radius=5,
                            color='rgba(0, 0, 0, 0.2)'
                        )
                    ),
                    width=660,
                    height=500,
                    margin=margin.all(10),
                    elevation=5
                ),
                Row([
                    ElevatedButton("Iniciar Webcam", on_click=lambda _: self.start_webcam()),
                    ElevatedButton("Detener Webcam", on_click=lambda _: self.stop_webcam())
                ])
            ]),
            padding=padding.all(20),
            bgcolor='blue',
            border_radius=10,
            expand=True,
        )
