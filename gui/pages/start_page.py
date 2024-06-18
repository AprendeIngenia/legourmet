from flet import *


class Start:
    def __init__(self, page):
        super().__init__()
        # GUI
        self.page = page
        self.page.theme = Theme(
            page_transitions=PageTransitionsTheme(
                android=PageTransitionTheme.FADE_UPWARDS,
                ios=PageTransitionTheme.CUPERTINO,
                macos=PageTransitionTheme.ZOOM,
                linux=PageTransitionTheme.ZOOM,
                windows=PageTransitionTheme.FADE_UPWARDS,
            )
        )

    def main(self):
        legourmet_watermark = Text(
            value="Legourmet by Geniia", font_family='Poppins', size=10, color='#FFFFFF')

        legourmet_title = Text(
            value="Legourmet", font_family='Poppins', size=72, weight='bold', color='#00FFA3')

        gradient_bg = LinearGradient(
            begin=alignment.top_left, end=alignment.bottom_right, colors=['#003e4b', '#0c0822'])

        start_button = Container(
            content=ElevatedButton(
                content=Container(
                    content=Column(
                        [Text(value="INICIAR", size=24, color='#008F5C', weight='bold',
                              font_family='Poppins')],
                        alignment=MainAxisAlignment.CENTER, spacing=3),
                    padding=padding.all(8)),
                on_click=self.start, bgcolor='#00FFA3'),
            padding=padding.symmetric(horizontal=2, vertical=2),
            border_radius=20)

        elements = Container(
            content=Column(
                [
                    Row([legourmet_watermark], alignment='start'),
                    Row([legourmet_title], alignment='center'),
                    Row([start_button], alignment='center')
                ],
            ),
            gradient=gradient_bg,
            expand=True
        )
        return elements

    def start(self, e):
        self.page.go("/welcome_page")
