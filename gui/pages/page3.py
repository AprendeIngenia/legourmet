import flet as ft

class Page3(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page        

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
                            ft.Text("¡Construye tu plato!", size=72, weight='bold', color='#00FFA3'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Text("Agrega un bloque que representa un ingrediente.", size=24, color='#FFFFFF'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Image(src="assets/robot.png", width=80, height=80),
                            ft.Text("→", size=48, color='#FFFFFF'),
                            ft.Image(src="assets/robot.png", width=80, height=80),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Text("Configúralos hasta sentir que has creado tu plato perfecto.", size=24, color='#FFFFFF'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Image(src="assets/robot.png", width=80, height=80),
                            ft.Text("+", size=48, color='#FFFFFF'),
                            ft.Image(src="assets/robot.png", width=80, height=80),
                            ft.Text("→", size=48, color='#FFFFFF'),
                            ft.Image(src="assets/robot.png", width=80, height=80),
                        ],
                        alignment='center'
                    ),
                   
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Image(src="assets/robot.png", width=100, height=100),
                                alignment=ft.alignment.center_left,  # Alinea la imagen a la izquierda
                                expand=True
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text("ARMA TU PLATO", size=32, color='#008F5C', weight='bold', font_family='Poppins'),
                                    on_click=self.on_accept_click,
                                    bgcolor='#00FFA3'
                                ),
                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                border_radius=20,
                                alignment=ft.alignment.center_right,  # Alinea el botón a la derecha
                                expand=True
                            )
                        ],
                        alignment='space_between',  # Distribuye el espacio entre los elementos
                        expand=True  # Asegura que el Row ocupe todo el espacio disponible
                    )
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
        self.page.go("/page4")
