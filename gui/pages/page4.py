import flet as ft
import cv2
import threading
import time
import base64

class Page4(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.capture = None
        self.image_control = ft.Image(src="/assets/icono.png", width=640, height=480)
        self.running = False

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Legourmet by Geniiia", size=24, color='#FFFFFF'),
                        ],
                        alignment='start'
                    ),
                    ft.Row(
                        [
                            ft.Text("¡Dale vida a tu creación!", size=72, weight='bold', color='#FF6F61'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Text("Una vez estés conforme con tu creación ingresa tu tablero a nuestro sistema para darle vida a tu plato.", size=24, color='#FFFFFF'),
                        ],
                        alignment='center'
                    ),                    
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Image(src="assets/robot.png", width=100, height=100),
                                alignment=ft.alignment.center_left,
                                expand=True
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text("ARMA TU PLATO", size=24, color='#008F5C', weight='bold', font_family='Poppins'),
                                    on_click=self.on_accept_click,
                                    bgcolor='#00FFA3'
                                ),
                                padding=ft.padding.symmetric(horizontal=10, vertical=10),
                                border_radius=20,
                                alignment=ft.alignment.center_right,
                                expand=True
                            ),
                            ft.Container(width=20),
                            ft.Card(
                                content=ft.Container(
                                    self.image_control,
                                    padding=0,
                                    border_radius=10,
                                    bgcolor='white',
                                    shadow=ft.BoxShadow(
                                        blur_radius=10,
                                        spread_radius=5,
                                        color='rgba(0, 0, 0, 0.2)'
                                    ),
                                    expand=True  # Asegurarse de que el contenedor expanda
                                ),
                                width=640,
                                height=480,
                                margin=ft.margin.all(10),
                                elevation=5
                            ),
                        ],
                        alignment='center',
                        expand=True
                    ),                    
                ],
                alignment='center',
                spacing=10
            ),
            padding=ft.padding.all(20),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=['#003e4b', '#0c0822']
            ),
            expand=True,
            width=self.page.window_width,
            height=self.page.window_height,
        )


    def on_accept_click(self, e):
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
            time.sleep(0.03) 

    def on_close(self):
        if self.cap:
            self.cap.release()