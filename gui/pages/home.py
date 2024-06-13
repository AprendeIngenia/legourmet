import flet as ft

class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.page.theme = ft.Theme(
            page_transitions=ft.PageTransitionsTheme(
                android=ft.PageTransitionTheme.FADE_UPWARDS,
                ios=ft.PageTransitionTheme.CUPERTINO,
                macos=ft.PageTransitionTheme.ZOOM,
                linux=ft.PageTransitionTheme.ZOOM,
                windows=ft.PageTransitionTheme.FADE_UPWARDS,
            )
        )

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Legourmet", size=72, weight='bold', color='#00FFA3'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text(value="INICIAR", size=32, color='#008F5C', weight='bold', font_family='Poppins')
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=3,
                                        ),
                                        padding=ft.padding.all(10),
                                    ),
                                    on_click=self.on_start_click,
                                    bgcolor='#00FFA3'
                                ),
                                padding=ft.padding.symmetric(horizontal=2, vertical=2),
                                border_radius=20,
                            )
                        ],
                        alignment='center'
                    )
                ],
                alignment='center',
                spacing=50
            ),
            padding=ft.padding.all(0),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=['#003e4b', '#0c0822']
            ),
            expand=True,
            width=self.page.window_width,
            height=self.page.window_height,
        )

    def on_start_click(self, e):
        print("Botón INICIAR clicado")  # Mensaje de depuración
        self.page.go("/page2")  # Redirige a la nueva página
        print("Redirigido a /page2")  # Mensaje de depuración
